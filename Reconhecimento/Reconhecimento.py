import cv2 as cv
import face_recognition as fr
import numpy as np
from Engine import get_nomes
ler = open("nomes.txt", "r")
linhas = ler.readlines()
num_linhas = len(linhas)

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
                nome = nomes_conhecidos[melhorid*num_linhas] #setar os nomes
            else:
                nome = "desconhecido"
            cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) #desenha um retangulo 
            cv.rectangle(frame, (left,bottom -35),(right,top),(0,0,255),2, cv.FILLED)
            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(frame, nome, (left+6,bottom-6),font,1.0,(255,255,255),1)
            print(nome)
        cv.imshow('Video', frame)
        k = cv.waitKey(10)
        if k == 27:
            break
    cam.release()
    cv.destroyAllWindows()
