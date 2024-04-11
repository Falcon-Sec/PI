import face_recognition as fr

nomes = []
fotos = []
def reconhece(localfoto): #função que reconhece os rostos nas fotos
    foto = fr.load_image_file(localfoto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos

    return False, []

def get_nomes():
    nomes_conhecidos = []
    rostos_conhecidos = []
    arqnomes = open("nomes.txt","r") #Abre o arquivo em modo leitura
    linhas = arqnomes.readlines() #Le as linhas do arquivo

    for linha in linhas: #Para cada linha
        linha = linha.strip() #remove a quebra de linha
        nomes.append(linha) #Coloca na variavel nomes
    arqnomes.close()

    arqfotos = open("fotos.txt","r") 
    linhasfoto = arqfotos.readlines()
    for linha in linhasfoto:
        linha = linha.strip()
        fotos.append(linha + ".png")
    arqfotos.close()
    for nome in nomes: #linka nome com foto
        for foto in fotos:
            reconhecido = reconhece(foto)
            if reconhecido [0]:
                rostos_conhecidos.append(reconhecido[1][0])
                nomes_conhecidos.append(nome)
    return rostos_conhecidos, nomes_conhecidos