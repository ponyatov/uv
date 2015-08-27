
import cv2 as cv

cam=cv.VideoCapture(0)

cv.namedWindow('cam',cv.CV_WINDOW_AUTOSIZE)
while cam.isOpened() and cv.waitKey(1)!=27: # ESC
    ret,frame=cam.read()
    cv.imshow('cam',frame)

cam.release()
cv.destroyAllWindows()
