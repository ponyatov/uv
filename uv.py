import cv2 as cv
cam=cv.VideoCapture(0)
if cam.isOpened():
    cv.namedWindow('cam')
    while cv.waitKey(1)!=27: # ESC
        ret,frame=cam.read()
        cv.imshow('cam',frame)
    cam.release()
    cv.destroyAllWindows()
