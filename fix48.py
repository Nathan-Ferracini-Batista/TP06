print("nathan Ferracini Batista, RA: 1051392411008")
def acrescimo():
  if salario <= 1500.00:
    print(salario*1.2)
  elif salario <= 2500.00:
    print(salario*1.1)
  else:
    print(salario*1.05)

salario = float(input("digite o salario: "))

acrescimo()