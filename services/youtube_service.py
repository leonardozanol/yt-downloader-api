from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError

from utils.file_utils import FileUtils
from exceptions.youtube_exceptions import InvalidURLYouTubeException, DownloadYouTubeException

class YouTubeService():
    def __init__(self, url: str, outputPath: str):
        self.url = url.strip()
        self.outputPath = outputPath


    def getVideo(self):
        try:

            youTubeVideo = YouTube(self.url)
            return youTubeVideo.streams.get_highest_resolution().download(output_path = self.outputPath), FileUtils.clearFileName(youTubeVideo.title)

        except RegexMatchError:
            raise InvalidURLYouTubeException("URL Invalida")

        except Exception as e:
            raise DownloadYouTubeException("Erro Ao Baixar Video") from e
        
    
    def getAudio(self):
        try:

            youTubeAudio = YouTube(self.url)
            return FileUtils.convertToMP3(youTubeAudio.streams.get_audio_only().download(output_path = self.outputPath)), FileUtils.clearFileName(youTubeAudio.title)

        except RegexMatchError:
            raise InvalidURLYouTubeException("URL Invalida")

        except Exception as e:
            raise DownloadYouTubeException("Erro Ao Baixar Audio") from e


