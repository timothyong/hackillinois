from flask import Flask
from flask import session,request,render_template, url_for, redirect
import cv2, time

app = Flask(__name__)
app.secret_key="lavaryss"

@app.route("/")
def test():
    count = 0;

    '''    time.sleep(5)
    webcam = cv2.VideoCapture()
    webcam.open(0)
    retval, image = webcam.retrieve()
    webcam.release()
    cv2.imwrite("test{0}.png".format(count), image)
    count += 1'''
    picture()
    return render_template("test.html")

def picture():
    count = 0;
    
    time.sleep(5)
    webcam = cv2.VideoCapture()
    webcam.open(0)
    retval, image = webcam.retrieve()
    webcam.release()
    cv2.imwrite("test{0}.png".format(count), image)
    count += 1

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=1337)
