from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from services.youtube_service import YouTubeService
from utils.file_utils import FileUtils
from core import config

router = APIRouter(prefix = "/v1", tags = ["YouTube"])

@router.get("/download/video")
def downloadVideo(url: str, backgroundTasks: BackgroundTasks):
    try:
        filePath, fileName = YouTubeService(url, config.FILES_DIR).getVideo()
        backgroundTasks.add_task(FileUtils.removeFile, filePath)

        return FileResponse(
            path = filePath,
            filename = fileName,
            media_type = "video/mp4"
        )

    except Exception as e:
        raise HTTPException(status_code = 400, detail = {'erro': str(e)})


@router.get("/download/audio")
def downloadAudio(url: str, backgroudTasks: BackgroundTasks):
    try:
        filePath, fileName = YouTubeService(url, config.FILES_DIR).getAudio()
        backgroudTasks.add_task(FileUtils.removeFile, filePath)

        return FileResponse(
            path = filePath,
            filename = fileName,
            media_type = "audio/mpeg"
        )

    except Exception as e:
        raise HTTPException(status_code = 400, detail = {'erro': str(e)})

