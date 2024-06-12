import Cadastro as cd
import Reconhecimento as rf
import os


x=1
while (x>0):
    os.system('cls')
    print("______    _               _____         _     \n|  ___|  | |             |_   _|       | |    \n| |_ __ _| | ___ ___  _ __ | | ___  ___| |__  \n|  _/ _` | |/ __/ _ \| '_ \| |/ _ \/ __| '_ \ \n| || (_| | | (__ (_) | | | | |  __/ (__| | | |\n\_| \__,_|_|\___\___/|_| |_\_/\___|\___|_| |_|\n")
    print("Oque deseja fazer: ")
    i = int(input("1-Reconhecimento \n2-Cadastro\n"))


    if i == 1:
        rf.reconhecimentofacial()
    elif i == 2:
        cd.cadastramento()
    else:
        print("Invalido")