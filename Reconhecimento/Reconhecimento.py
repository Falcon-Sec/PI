import cv2 as cv
import face_recognition as fr
import numpy as np
from Engine import get_nomes

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
            else:
                nome = "desconhecido"
            cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) #desenha um retangulo 
            print(nome)
        cv.imshow('Video', frame)
        k = cv.waitKey(5)
        if k == 27:
            break
    cam.release()
    cv.destroyAllWindows()

