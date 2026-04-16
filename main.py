from fastapi import FastAPI
from controllers import youtube_controller
from utils.file_utils import FileUtils
from core import config

FileUtils.createDir(config.FILES_DIR)

app = FastAPI()
app.include_router(youtube_controller.router)

