import cv2 as cv

def get_foto():
    #ler quantas linhas tem a lista nomes
    quant = open("nomes.txt", "r")
    nomes = quant.readlines()
    num_linhas = len(nomes)

    cam = cv.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv.imshow('camera', frame)
        k = cv.waitKey(5)
        if k == 27:
            break
        cv.imwrite(f"{num_linhas}.png", frame)
    cam.release()
    cv.destroyAllWindows()
