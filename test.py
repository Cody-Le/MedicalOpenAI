import requests


url = "http://127.0.0.1:5000/process"


files = {"imagefile": open("test_files/img-sample-consolidated-medical-record-summ.jpg", "rb")}

r = requests.post(url, files=files)
print(r.text)