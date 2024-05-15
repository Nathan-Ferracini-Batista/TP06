print("Nathan Ferracini Batista - 1051392411008")
peso= float(input("Digite seu peso:"))
altura= float(input("Digite a altura em metros:"))
sexo= input("Digite M para masculino ou F pra feminino:")
R = peso/(altura*altura)
print("O seu IMC é",R)
def calculoIMC(R,sexo):
    if(sexo == "M" or sexo == "m"):
        if(round(R)<20):
            print("Você está abaixo do peso ideal!")
        elif(round(R)>=20 and R<25):
            print("Você está no peso ideal!")
        else:
            print("Você está acima do peso!")
    
    if(sexo == "F" or sexo == "f"):
        if(round(R)<19):
            print("Você está abaixo do peso ideal!")
        elif(round(R)>=19 and R<24):
            print("Você está no peso ideal!")
        else:
            print("Você está acima do peso!")
calculoIMC(R,sexo)