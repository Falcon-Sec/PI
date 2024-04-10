import face_recognition as fr

def reconhece(localfoto):
    foto = fr.load_image_file(localfoto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos

    return False, []


def get_nomes():
    rostos_conhecidos = []
    nomes_conhecidos = []

    ramon = reconhece('foto.png')
    if(ramon[0]):
        rostos_conhecidos.append(ramon[1][0])
        nomes_conhecidos.append("ramon")

    erik =  reconhece('foto2.png')
    if(erik[0]):
        rostos_conhecidos.append(erik[1][0])
        nomes_conhecidos.append("erik")

    higor = reconhece('foto3.png')
    if (higor[0]):
        rostos_conhecidos.append(higor[1][0])
        nomes_conhecidos.append("higor")
    maurisio = reconhece('foto4.png')

    return rostos_conhecidos, nomes_conhecidos
