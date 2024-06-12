import cv2 as cv
import face_recognition as fr
import numpy as np
from Engine import get_nomes
import serial
import time

ser = 1 #serial.Serial('COM3', 9800, timeout=1)#Conecta ao arduíno

def reconhecimentofacial(): 
    cam = cv.VideoCapture(0) #usa a camera
    rostos_conhecidos, nomes_conhecidos = get_nomes() #puxa os dados
    if not cam.isOpened():
        print("Camera not opened")
    while True:
        ret, frame = cam.read() #armazena frame por frame
        faces = fr.face_locations(frame)
        desconhecidos = fr.face_encodings(frame, faces) #codifica os rostos
        for(top, right, bottom, left), desconhecidos in zip(faces, desconhecidos):
            resultado = fr.compare_faces(rostos_conhecidos, desconhecidos) #compara os rostos armazenados e os visualizados
            distancia = fr.face_distance(rostos_conhecidos, desconhecidos)
            melhorid = np.argmin(distancia) #define a melhor comparação
            if resultado[melhorid]:
                nome = nomes_conhecidos[melhorid] #setar os nomes
                ser.write(b'G')
                time.sleep(3)
                ser.write(b'S')
            else:
                nome = "desconhecido"
                ser.write(b'R')
                time.sleep(3)
                ser.write(b'S')
            print(nome)
            #if nome != "desconhecido":
                #ser.write(b'H')
                #time.sleep(3)
                #ser.write(b'L')

        cv.imshow('Video', frame)
        k = cv.waitKey(5)
        if k == 27:
            break
    cam.release()
    cv.destroyAllWindows()
