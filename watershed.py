__author__ = 'Miguel Araujo'


import sys
import cv2
import numpy as np
import utilities as u



isNewPoint = 0
newPoint = (-1,-1)


def onMouse(event, x, y, flags, params):
    global isNewPoint
    global newPoint
    if event == cv2.EVENT_LBUTTONUP:
        isNewPoint=1
        newPoint = (x,y)




def main(argv):
    global isNewPoint
    global newPoint

    img = cv2.imread("Penguins.jpg")
    img = u.resize(img)

    winName="watershed Testes"
    imgPrev = np.copy(img)
    cv2.namedWindow(winName)

    cv2.imshow(winName, imgPrev)
    cv2.setMouseCallback(winName, onMouse)

    op='f'
    fgRect=[]
    bgRect=[]
    while op!='p' and op!='P':
        op = cv2.waitKey(50)
        if isNewPoint == 1:
            isNewPoint=0
            if op == 'f' or op == 'F':
                fgRect+=[newPoint]
            elif op == 'f' or op == '':
                pass

    cv2.destroyAllWindows()
    #img = cv2.imread("5.jpg")
    #imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #fgbf = np.zeros((img.shape[0],img.shape[1],1), np.uint8)

    #bg
    #cv2.rectangle(fgbf,(0,149),(57,663), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #cv2.rectangle(fgbf,(0,0),(999,148), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #cv2.rectangle(fgbf,(959,149),(999,663), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #cv2.rectangle(fgbf,(386,355),(828,438), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #fg
    #cv2.rectangle(fgbf,(161,523),(890,568), (255,255,255),thickness=cv2.cv.CV_FILLED)

    #bg
    #cv2.rectangle(fgbf,(0,0),(999,49), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #cv2.rectangle(fgbf,(959,50),(999,651), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #cv2.rectangle(fgbf,(0,50),(57,651), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #cv2.rectangle(fgbf,(0,652),(999,749), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #cv2.rectangle(fgbf,(533,434),(833,476), (128,128,128), thickness=cv2.cv.CV_FILLED)
    #fg
    #cv2.rectangle(fgbf,(439,551),(916,596), (255,255,255),thickness=cv2.cv.CV_FILLED)



    #marker32 = np.int32(fgbf)

    #cv2.watershed(img,marker32)
    #m = cv2.convertScaleAbs(marker32)

    #u.showImg(m,"m")


    #ret,thresh = cv2.threshold(m,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #res = cv2.bitwise_and(img,img,mask = thresh)



if __name__ == "__main__":
    main(sys.argv)