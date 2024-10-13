import os,sys
from workerSafety.logger import logging
from workerSafety.exception import CustomException
from workerSafety.pipeline.training_pipeline import TrainPipeline
from workerSafety.utils.main_utils import encodeImageIntoBase64,decodeImage
from flask import Flask, request,jsonify, render_template,Response
from flask_cors import CORS, cross_origin

from workerSafety.constant.application import APP_HOST, APP_PORT  

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(imgstring=image, fileName=wsapp.filename)

        os.system("cd yolov5/ && python detect.py --weights last.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg")

        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf yolov5/runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        raise CustomException(e,sys)

    return jsonify(result)

@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera starting!!" 

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")

if __name__ == "__main__":
    wsapp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT,debug=True)