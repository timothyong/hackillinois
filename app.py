from flask import Flask
from flask import session,request,render_template, url_for, redirect
import cv2, time

app = Flask(__name__)
app.secret_key="lavaryss"

@app.route("/")
def home():
    count = 0;
    while(1):
        time.sleep(5)
        webcam = cv2.VideoCapture()
        webcam.open(0)
        retval, image = webcam.retrieve()
        webcam.release()
        cv2.imwrite("test{0}.png".format(count), image)
        count++
