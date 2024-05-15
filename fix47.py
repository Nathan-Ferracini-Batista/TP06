print("nathan Ferracini Batista, RA: 1051392411008")
def numero():
 if valor %10 == 0:
  print("\nÉ divisivel por 10")
 elif valor % 5 == 0:
  print("\nÉ divisivel por 5")
 elif valor % 2 == 0:
  print("\nÉ divisivel por 2")
 else:
  print("\nNão é divisivel por 10, 5 ou 2")

valor = int(input("Digitar um valor: "))
numero()