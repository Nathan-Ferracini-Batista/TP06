print("nathan Ferracini Batista, RA: 1051392411008")
import math
def calculo(valor):
  if (valor == 1) or (valor == 2):
    print(valor**2)
  elif valor == 3:
    print(math.factorial(valor))
  elif  (valor == 4) or (valor == 5) or (valor == 7) or (valor == 8):
    print(valor/9)

valor = int(input("digite um numero: "))
calculo(valor)