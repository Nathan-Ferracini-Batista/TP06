print("Nathan Ferracini Batista - 1051392411008")

nome = input("digite seu nome:")
status = int(input("Digite 0 se for aluno ou digite 1 se for professor:"))

if(status==0):
  print("Alunos não tem permissão para usar este aplicativo")
elif(status==1):
 
  np1 = float (input("digite a primeira nota: "))
  np2 = float (input("digite a segunda nota: "))
  media = (np1*4 + np2*6)/10
  def calculo(mediageral):
    if media <=10 and media>=9:
      print("Conceito:A Aprovado")
    elif media <9 and media >=7:
      print("Conceito:B Aprovado")
    elif media <7 and media >=3:
      print("Conceito:C Exame")
    elif media <3:
      print("conceito:D DP")
  calculo(media)