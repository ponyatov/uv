import cv2 as cv
import winsound as snd
cam=cv.VideoCapture(0)
cascade = cv.CascadeClassifier("lbpcascade_frontalface.xml") 
if cam.isOpened():
    ret,frame=cam.read()
    shape=frame.shape
    

    cv.namedWindow('cam')
    while cv.waitKey(1)!=27: # ESC
        ret,frame=cam.read()
#         frame=cv.detailEnhance(frame, sigma_s=10, sigma_r=0.15)
#         frame=cv.edgePreservingFilter(frame, flags=1, sigma_s=60, sigma_r=0.4)
#         bw,frame=cv.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
#         frame=cv.stylization(frame, sigma_s=60, sigma_r=0.07)
        gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        rects = cascade.detectMultiScale(gray, scaleFactor=1.3, 
            minNeighbors=4, minSize=(40, 40))#, 
#             flags=cv.CV_HAAR_SCALE_IMAGE)
        for x, y, w, h in rects:
            snd.Beep(888,88)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2) 
        cv.imshow('cam',frame)
    cam.release()
    cv.destroyAllWindows()
