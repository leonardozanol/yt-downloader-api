from pytubefix import YouTube
import os

from utils.file_utils import FileUtils

class YouTubeService():
    def __init__(self, url: str, outputPath: str):
        self.url = url.strip()
        self.outputPath = outputPath


    def getVideo(self):
        try:

            youTubeVideo = YouTube(self.url)
            return youTubeVideo.streams.get_highest_resolution().download(output_path = self.outputPath), FileUtils.clearFileName(youTubeVideo.title)

        except Exception as e:
            raise Exception("Erro Ao Baixar Video: " + str(e))
        
    
    def getAudio(self):
        try:

            youTubeAudio = YouTube(self.url)
            return FileUtils.converToMP3(youTubeAudio.streams.get_audio_only().download(output_path = self.outputPath)), FileUtils.clearFileName(youTubeAudio.title)

        except Exception as e:
            raise Exception("Erro Ao Baixar Audio: " + str(e))

