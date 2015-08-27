
import cv2 as cv

cam=cv.VideoCapture(0)

cv.namedWindow('cam',cv.CV_WINDOW_AUTOSIZE)
while cam.isOpened():
    ret,frame=cam.read()
    cv.imshow('cam',frame)
    cv.waitKey(1)

cam.release()
cv.destroyAllWindows()
