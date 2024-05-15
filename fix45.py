print("nathan Ferracini Batista, RA: 1051392411008")
def desconto(num):
  if num >=300.00:
    print(num*0.8)
  elif num >=200.00:
    print(num*0.9)
  else:
    print(num*0.95)
    
total = 0
while True:
  valor = float(input("digite o valor da compra(digite 0 para parar):"))
  if valor == 0:
    break
  else:
    total += valor
    continue

desconto(total)