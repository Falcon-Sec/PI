from TirarFoto import get_foto

def cadastramento(): 
    nome1 = input('Digite seu nome: ') #Scan de nome

    arqnomes = open("nomes.txt","a") #Abre o arquivo nome em modo edição
    arqfotos = open("fotos.txt","a")

    arqnomes.write(nome1+"\n") #Escreve o nome + quebra de linha
    arqnomes.close() #Fecha o arquivo

    #escrever o numero.png no fotos.txt
    quant = open("nomes.txt", "r")
    quantnomes = quant.readlines()
    num_linhas = len(quantnomes)
    arqfotos.write(f"{num_linhas}"+"\n")
    arqfotos.close()

    get_foto()

