from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable, MembersOnly, AgeRestrictedError

from utils.file_utils import FileUtils
from exceptions.youtube_exceptions import InvalidURLYouTubeException, ObjectYouTubeNotFoundException, ObjectYouTubePrivateException

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
        
        except VideoUnavailable:
            raise ObjectYouTubeNotFoundException("Nao Foi Possivel Encontrar Video")
        
        except MembersOnly:
            raise ObjectYouTubePrivateException("Nao Foi Possivel Obter Video Privado")
        
        except AgeRestrictedError:
            raise ObjectYouTubePrivateException("Nao Foi Possivel Obter Video Restrito")
        
        except Exception:
            raise
        
    
    def getAudio(self):
        try:

            youTubeAudio = YouTube(self.url)
            return FileUtils.convertToMP3(youTubeAudio.streams.get_audio_only().download(output_path = self.outputPath)), FileUtils.clearFileName(youTubeAudio.title)

        except RegexMatchError:
            raise InvalidURLYouTubeException("URL Invalida")
        
        except VideoUnavailable:
            raise ObjectYouTubeNotFoundException("Nao Foi Possivel Encontrar Audio")
        
        except MembersOnly:
            raise ObjectYouTubePrivateException("Nao Foi Possivel Obter Audio Privado")
        
        except AgeRestrictedError:
            raise ObjectYouTubePrivateException("Nao Foi Possivel Obter Audio Restrito")
        
        except Exception:
            raise


