import cv2

capture =cv2.VideoCapture(0)
face_haar_cascade =cv2.CascadeClassifier('haarcascade_')

while True:
    _, image= capture.read()
    gray=cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)
    

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h))
    