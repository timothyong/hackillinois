import cv2
import sys
import matplotlib.pyplot as pt
import numpy as np
import numpy.linalg as la
import math as mt

#Content of out eigens
#	there would be five images of each person
#	the collumns would be the frob norm of each type
#	4 rows for each person
#	1)Smiling
#	2)Sad
#	3)Serious
#	4)Blank
#	5)If wearing specs then without specs
#	6)looking left
#	7)looking right
ournorms = {'Abhishek':[5916.56,6155.725,5835.83,6033.245,5922.402,6207.052,6028.91],
			'Akshay':[6268.704,6335.443,6119.169,6277.252,6126.155,6232.754,6294.937],
			'Chris':[6479.241,6297.295,6477.624,6463.082,6385.727,6275.596,6200.595],
			'Tim':[6507.45,6569.225,6637.975,6731.95,6546.934,6239.888,6529.477]}

indbuffervals = {'Abhishek':100,
				 'Akshay':100,
				 'Chris':50,
				 'Tim':50}
#hardcode values into ournorms above


def recognizeFace(faces):
	retval = True
	if(len(faces)>10):
		print("Fuck it too many faces shoot everyone")
		return True, 100
	for i in range(faces.shape[0]):
		x, y, w, z = faces[i]
		bufw = (400 - w)/2
		bufh = (400 - h)/2
		inmod = image[y-bufw:y+w+bufw,x-bufh:x+h+bufh]
		retwhat = checker(inmod)
		retval = retwhat and retval
	return retval,len(faces)


def checker(inmod):
	tempnorm = la.norm(inmod)
	retval = False
	for name,val in ournorms.iteritems():
		for j in val:
			if(np.abs(j-tempnorm)<indbuffervals[name]):
				retval = True;
				print("is")
				print(name)
				break
		if(not retval):
			print("not")			
			print(name)
	return retval

# Get values from command line
def check(image):
	#imagePath = sys.argv[1]
	#cascPath = sys.argv[2]
	imagePath = image
	cascPath = "haarcascade_frontalface_default.xml"


	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)

	# Read the image
	image = cv2.imread(imagePath)
	imnonmod = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
    	gray,
    	scaleFactor=1.25,
    	minNeighbors=5,
    	minSize=(40, 40)    
	)

	print "Found {0} faces!".format(len(faces))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
    	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if(len(faces)>0):
	what, number = recognizeFace(faces)
	# return what to the arduino
	if(what is False):
		print("intruder detected")


	cv2.imshow("Faces found", image)
	#cv2.waitKey(0)




