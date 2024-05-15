# Programa para cadastrar 3 e-mails

# Lista para armazenar os e-mails
emails_cadastrados = []

# Função para cadastrar e-mail
def cadastrar_email():
  email = input("Digite um e-mail para cadastro: ")
  emails_cadastrados(email)


# Loop para cadastrar 3 e-mails
for i in range(3):
  cadastrar_email()

# Exibindo os e-mails cadastrados
  print("E-mails cadastrados:")
for email in emails_cadastrados:
  print(email)
