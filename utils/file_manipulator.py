import os
import re

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


