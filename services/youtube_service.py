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
            return yt_obj.streams.get_highest_resolution().download(output_path = self.outputPath), FileUtils.clearFileName(yt_obj.title)

        except Exception as e:
            raise Exception("Ero ao Baixar Video: " + str(e))


    def getAudio(self):
        pass


