from flask import Flask, request
from flask_cors import CORS
import base64
from main import process_image

app = Flask("app")
CORS(app)


@app.route("/")
def home():
    return "use /process to use the functions"


@app.route("/process", methods = ["POST"])
def process():
    if(request.method == "POST"):
        image = request.files.get("imagefile", "")
        print(image)
        b64_image = base64.b64encode(image.read()).decode("utf-8")
        response = process_image(b64_image)
        return response["message"]["content"]