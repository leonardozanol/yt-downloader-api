import os
import re
import subprocess

class FileUtils():
    @staticmethod
    def createDir(path: str):
        try:
            os.makedirs(path, exist_ok = True)
            return True
    
        except Exception as e:
            print(e)
            return False


    @staticmethod
    def removeFile(filePath: str):
        try:
            if os.path.exists(filePath):
                os.remove(filePath)
                return True

            return False

        except Exception as e:
            print(e)
            return False


    @staticmethod
    def clearFileName(fileName: str):
        return re.sub(r'[\\/*?:"<>|]', "", fileName).strip()
    
    @staticmethod
    def converToMP3(path: str):
        try:
            outputPath = path.rsplit(".", 1)[0] + ".mp3"

            subprocess.run(["ffmpeg", "-i", path, "-vn", "-ab", "192k", "-ar", "44100", "-y", outputPath], check = True)
            
            if os.path.exists(outputPath):
                return outputPath

            return path

        except Exception as e:
            print(e)
            return path

