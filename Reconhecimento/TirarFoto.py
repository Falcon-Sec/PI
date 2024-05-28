import cv2 as cv
import numpy as np
import urllib.request

def get_foto():
    #ler quantas linhas tem a lista nomes
    quant = open("nomes.txt", "r")
    nomes = quant.readlines()
    num_linhas = len(nomes)

    url = 'http://192.168.172.168/cam-hi.jpg'
    cv.namedWindow("camera",cv.WINDOW_AUTOSIZE)
    
    while True:
        img= urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img.read()),dtype=np.uint8)
        cam = cv.imdecode(imgnp,-1)
        cv.imshow('camera', cam)
        k = cv.waitKey(5)
        if k == 27:
            break
        cv.imwrite(f"{num_linhas}.png", cam)
    cv.destroyAllWindows()
