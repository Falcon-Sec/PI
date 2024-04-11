import Cadastro as cd
import Reconhecimento as rf

print("---FalconTech----")
print("Oque deseja fazer: ")
i = int(input("1-Reconhecimento \n2-Cadastro\n"))

if i == 1:
    rf.reconhecimentofacial()
elif i == 2:
    cd.cadastramento()
else:
    print("Invalido")