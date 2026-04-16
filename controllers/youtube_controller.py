from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from services.youtube_service import YouTubeDownloader
from utils.file_utils import FileUtils
from core import config

router = APIRouter(prefix = "/v1", tags = ["YouTube"])

@router.get("/download/video")
def downloadVideo(url: str, backgroundTasks: BackgroundTasks):
     video = YouTubeDownloader(url, config.FILES_DIR).getVideo()
     
     if not video["success"]:
         raise HTTPException(status_code = 404, detail = "Nao Foi Possivel Baixar Video")

     backgroundTasks.add_task(FileUtils.removeFile, video["filePath"])

     return FileResponse(
             path = video["filePath"],
             filename = video["fileName"],
             media_type="video/mp4"
     )


@router.get("/download/audio")
def downloadAudio(url: str):
    audio = YouTubeDownloader(url, config.FILES_DIR).getAudio()

    if not audio["success"]:
        raise HTTPException(status_code = 404, detail = "Nao Foi Possivel Baixar Audio")

    return audio


