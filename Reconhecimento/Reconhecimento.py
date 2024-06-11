import cv2 as cv
import face_recognition as fr
import numpy as np
import urllib.request
from Engine import get_nomes
import serial

ser = serial.Serial('COM3',  115200)

def reconhecimentofacial(): 
    url = 'http://192.168.63.168/cam-hi.jpg' #url da camera esp32
    #cv.namedWindow("camera",cv.WINDOW_AUTOSIZE)
    rostos_conhecidos, nomes_conhecidos = get_nomes() #puxa os dados da engine
    while True:
        img= urllib.request.urlopen(url) #abre o url
        imgnp=np.array(bytearray(img.read()),dtype=np.uint8) 
        frame = cv.imdecode(imgnp,-1)
        faces = fr.face_locations(frame)
        desconhecidos = fr.face_encodings(frame, faces) #codifica os rostos
        for(top, right, bottom, left), desconhecido in zip(faces, desconhecidos):
            resultado = fr.compare_faces(rostos_conhecidos, desconhecido) #compara os rostos armazenados e os visualizados
            distancia = fr.face_distance(rostos_conhecidos, desconhecido)
            melhorid = np.argmin(distancia) #define a melhor comparação
            if resultado[melhorid]:
                nome = nomes_conhecidos[melhorid] #setar os nomes
            else:
                nome = "desconhecido"
            print(nome) #printa o nome na terminal
            if nome != "desconhecido":
                ser.write(b'H')

cv.destroyAllWindows()
reconhecimentofacial()

