import os 
#Variaveis
funcionario:str;
kids:int;
adultos:int;
jovens:int;
universitystudent:int;
totalespaco:int;
idade:int;

#menu inicial (protopico de ideia)
print("Infomer lotação maxima do CUCA");
totalespaco = input();
os.system("cls") #limpa tela 

print("-------------Entradas Visitante--------------");
print("");
print("Nome: ",end="");
nome = input();
print("idade: ",end="");
idade = int(input());
os.system("cls") 

if idade >= 1 and idade <= 9:
    print("\nCategoria:Crianças");
    print("Valor:Gratis");
    kids=+1;

if idade >=10 and idade <=17:
    print("\nCategoria:Adolecentes");
    print("Valor:$15,00");
    jovens=+1;

if idade >=18:
    print("\nCategoria:Adultos");
    print("Valor:$40,00\n\n");
    desconto=int(input("Desconto:[1]Sim  [2]não: "));
    if desconto ==1:#PRECISA FZR VERIFICAÇÃO DA MATRICULA AINDA
         print("\nCategoria:Adultos/Estudande Universiatrio");
         print("Valor:$20,00");
    else:
        print("\nCategoria:Adultos");
        print("Valor:$40,00");

