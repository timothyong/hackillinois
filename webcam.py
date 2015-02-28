import cv2, time

count = 0;
while(1):
    time.sleep(5)
    webcam = cv2.VideoCapture()
    webcam.open(0)
    retval, image = webcam.retrieve()
    webcam.release()
    cv2.imwrite("static/images/test{0}.png".format(count), image)
    count += 1
