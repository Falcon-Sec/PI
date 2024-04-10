import cv2 as cv
import face_recognition as fr
import numpy as np
from fotos import get_nomes

cam = cv.VideoCapture(0)
rostos_conhecidos, nomes_conhecidos = get_nomes()
if not cam.isOpened():
    print("Camera not opened")
while True:
    ret, frame = cam.read()
    faces = fr.face_locations(frame)
    desconhecidos = fr.face_encodings(frame, faces)
    for(top, right, bottom, left), desconhecidos in zip(faces, desconhecidos):
        resultado = fr.compare_faces(rostos_conhecidos, desconhecidos)
        print(resultado)
        distancia = fr.face_distance(rostos_conhecidos, desconhecidos)
        melhorid = np.argmin(distancia)
        if resultado[melhorid]:
           nome = nomes_conhecidos[melhorid]
        else:
            nome = "desconhecido"
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        print(nome)
    cv.imshow('Video', frame)
    k = cv.waitKey(5)
    if k == 27:
        break
cam.release()
cv.destroyAllWindows()

