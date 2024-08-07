import requests
import base64

url = "http://127.0.0.1:5000/process"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")



files = {"imagefile": open("test_files/img-sample-consolidated-medical-record-summ.jpg","rb")}

r = requests.post(url, files=files)
print(r.text)