from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
import logging

from exceptions.youtube_exceptions import InvalidURLYouTubeException, ObjectYouTubeNotFoundException, ObjectYouTubePrivateException
from services.youtube_service import YouTubeService
from utils.file_utils import FileUtils
from core import config

router = APIRouter(prefix = "/v1", tags = ["YouTube"])
logger = logging.getLogger(__name__)

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

    except InvalidURLYouTubeException:
        raise HTTPException(status_code = 400, detail = "URL Invalida")

    except ObjectYouTubeNotFoundException as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
    except ObjectYouTubePrivateException as e:
        raise HTTPException(status_code = 403, detail = str(e))

    except Exception:
        logger.exception("Erro Inesperado ao baixar Video")
        raise HTTPException(status_code = 500, detail = "Erro Interno ao processar video")


@router.get("/download/audio")
def downloadAudio(url: str, backgroundTasks: BackgroundTasks):
    try:
        filePath, fileName = YouTubeService(url, config.FILES_DIR).getAudio()
        backgroundTasks.add_task(FileUtils.removeFile, filePath)

        return FileResponse(
            path = filePath,
            filename = fileName,
            media_type = "audio/mpeg"
        )

    except InvalidURLYouTubeException:
        raise HTTPException(status_code = 400, detail = "URL Invalida")

    except ObjectYouTubeNotFoundException as e:
        raise HTTPException(status_code = 404, detail = str(e))
    
    except ObjectYouTubePrivateException as e:
        raise HTTPException(status_code = 403, detail = str(e))

    except Exception:
        logger.exception("Erro Inesperado ao baixar Audio")
        raise HTTPException(status_code = 500, detail = "Erro Interno ao processar Audio")

