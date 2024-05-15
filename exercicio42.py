print("Nathan Ferracini Batista - 1051392411008")
def Maior (n1,n2,n3,n4,n5):
    if(n1>n2 and n1>n3 and n1>n4 and n1>n5):
        print("A primeira nota é a maior",n1)
    elif(n2>n1 and n2>n3 and n2>n4 and n2>n5):
        print("A segunda nota é a maior",n2)
    elif(n3>n1 and n3>n2 and n3>n4 and n3>n5):
        print("A terceira nota é a maior",n3)
    elif(n4>n1 and n4>n2 and n4>n3 and n4>n5):
        print("A quarta nota é a maior",n4)
    elif(n5>n1 and n5>n2 and n5>n3 and n5>n4):
        print("A quinta nota é a maior",n5)
    else:
        print("Notas inválidas")
 
cont= 1
while (cont<=5):
    if(cont == 1):
        n1= float(input("Digite a primeira nota:"))
        cont= cont+1
    elif(cont == 2):
        n2= float(input("Digite a segunda nota:"))
        cont= cont+1
    elif(cont==3):
        n3= float(input("Digite a terceira nota:"))
        cont= cont+1
    elif(cont==4):
        n4= float(input("Digite a quarta nota:"))
        cont= cont+1
    elif(cont==5):
        n5= float(input("Digite a quinta nota:"))
        break
 
Maior(n1,n2,n3,n4,n5)
 


