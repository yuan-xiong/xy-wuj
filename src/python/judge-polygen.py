import numpy as np
import cv2 as cv

# https://blog.csdn.net/weixin_45668655/article/details/103922317

image = "../data/shapes.png"
img = cv.imread(image)
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,thresh = cv.threshold(imgGray,170,255,cv.THRESH_BINARY_INV)
contours,_ = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

# approx polygen
for contour in contours:
    approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
    cv.drawContours(img,[approx],0,(0,0,0),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv.putText(img,"Triangle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    elif len(approx) == 4: 
        x1,y1,w,h = cv.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio) 

		# Square or Rectangle ?
        if aspectRatio >= 0.95 and aspectRatio <= 1.15:
            cv.putText(img,"Square",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
        else:   
            cv.putText(img,"Rectangle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    else:
        cv.putText(img,"Circle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
        
cv.imshow("shapes",img)

cv.waitKey(0)
cv.destroyAllWindows()

