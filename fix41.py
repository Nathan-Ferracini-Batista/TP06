print("nathan Ferracini Batista, RA: 1051392411008")
import math
def contas(valor):

    if valor in [ 1,2,3]:
      return valor**2
    elif valor in [4,9]:
      return math.sqrt (valor)
    elif valor in [6,7,8]:
      return valor/9
    else:
       return "valor invalido"
valor = int(input("digite o valor: "))
print(contas(valor))
