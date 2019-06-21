import requests
import io
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    ret, jpeg = cv2.imencode('.jpg', frame)
    bio = io.BytesIO()
    bio.write(jpeg)
    bio.seek(0)
    r = requests.post("http://127.0.0.1:8081", files={"image":bio}, headers={'filename':'myfile.py', 'listener':'myimage_receiver', 'listener_function':'ondata'})
    print(r.status_code, r.reason)
