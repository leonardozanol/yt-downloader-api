from pytubefix import YouTube
import os

from utils.file_utils import FileUtils

class YouTubeDownloader():
    def __init__(self, url: str, outputPath: str):
        self.url = url.strip()
        self.outputPath = outputPath

    def getVideo(self):
        try:
            yt_obj = YouTube(self.url)

            return {"success": True, "filePath": yt_obj.streams.get_highest_resolution().download(output_path = self.outputPath), "fileName": FileUtils.clearFileName(yt_obj.title)}

        except Exception as e:
            print(e)
            return {"success": False}


    def getAudio(self):
        try:
            yt_obj = YouTube(self.url)
            return {"success": True, "filePath": yt_obj.streams.get_audio_only().download(output_path = self.outputPath), "title": FileUtils.clearFileName(yt_obj.title)}

        except Exception as e:
            print(e)
            return {"success": False}


