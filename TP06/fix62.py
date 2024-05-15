senhas_cadastrads = []

def cadastrar_senha():
  senha = input("digite uma senha para cadastro: ")
  senhas_cadastrads(senha)

for i in range(5):
  cadastrar_senha()

print("senhas cadastradas: ")
for senha in senhas_cadastrads:
  print(senha)

