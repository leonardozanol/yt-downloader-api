from pytubefix import YouTube
import os

from utils.file_utils import FileUtils
from modells.youtube_enum import TypeObject

class YouTubeService():
    def __init__(self, url: str, typeObject: TypeObject, outputPath: str):
        self.url = url.strip()
        self.typeObject = typeObject
        self.outputPath = outputPath

    def getObject(self):
        try:
            
            youTubeObject = YouTube(self.url)

            if self.typeObject == TypeObject.VIDEO:
                streamsType = youTubeObject.streams.get_highest_resolution() 

            else:
                streamsType = youTubeObject.streams.get_audio_only()

            return streamsType.download(output_path = self.outputPath), FileUtils.clearFileName(youTubeObject.title)

        except Exception as e:
            raise Exception("Erro ao Baixar: " + str(e))

