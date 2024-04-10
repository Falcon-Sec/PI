import cv2 as cv

cam = cv.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv.imshow('camera', frame)
    k = cv.waitKey(5)
    if k == 27:
        break
    cv.imwrite('foto4.png', frame)
cam.release()
cv.destroyAllWindows()
