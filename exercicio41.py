def calcular_fatorial(n):
  fatorial = 1
  for i in range (1, n+1):
    fatorial *=i
  print(fatorial)
  return fatorial
n=int(input("digite um numero: "))
calcular_fatorial(n)