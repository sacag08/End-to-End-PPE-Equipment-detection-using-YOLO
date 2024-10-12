import os
import sys
import yaml
import base64

from WorkerSafety.exception import CustomException
from WorkerSafety.logger import logging

def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            logging.info("Read yaml file seccessfully")
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise CustomException(e,sys)

def write_yaml_file(file_path: str,content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        os.makedirs(file_path,exist_ok=True)
        with open(file_path) as file:
            yaml.dump(content,file)
            logging.info("Seccessfully written yaml file")
    except Exception as e:
        raise CustomException(e,sys)
    
def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/",fileName,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb') as f:
        return base64.b64encode(f.read())

    

