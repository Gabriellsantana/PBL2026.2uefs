import os #importando bibiotleca para cls

#Variaveis
funcionario:str;
kids:int;
adultos:int;
jovens:int;
universitystudent:int;
lotacaoMax:int;
idade:int;
senha:str;
contLotacao:int;
contLotacao=0;
#menu inicial
print("-------------Bem Vindo Organização do Cuca-------------");
print("Infomer Capacidade máxima: ",end="");
lotacaoMax = int(input());
senha=input("Crie um senha para o dia: ");

  
os.system("cls") #limpa tela 

opcao =""
while opcao!= "2": #laço principal de repetição do menu
    print("-------------Entradas Visitante--------------");
    print("[1]Vender");
    print("[2]Encerra\n");
    opcao =input()
    os.system("cls") 

    match opcao:
     case "1":
        if contLotacao <= lotacaoMax:#Inicio controle para lotação maxima do espaço
           print("Idade do visitante: ",end="");
           idade = int(input());

           if idade >=1 and idade <=9:
              print("INGRESSO VENDIDO");
              print("Categira:Kids");
              print("Valor:Grâtis\n");
              contLotacao+=1;
              print("ingressos vendidos:%d"%contLotacao);
              print("Capacidade local:%d"%lotacaoMax);
           
           elif idade >=10 and idade <=17:  
              print("INGRESSO VENDIDO");
              print("Categoria:Adolecente");
              print("Valor:15$\n");
              contLotacao+=1

           elif idade >=18:
              print("Estudande Universitario Uefs:")  
              uefs=int(input("[1]sim----[2]Não"));
              if uefs ==1:# controle estudandte
                 print("INGRESSSO VENDIDO");
                 print("Categoria:Estudante");
                 print("Valor:20$\n");
                 contLotacao+=1
                 print("ingressos vendidos:%d"%contLotacao);
                 print("Capacidade local:%d"%lotacaoMax);
              else:#fim controle estudande
                 print("INGRESSO VENDIDO");
                 print("Categoria:Adulto");
                 print("Valor:40$\n\n");
                 contLotacao+=1
                 print("ingressos vendidos:%d"%contLotacao);
                 print("Capacidade local:%d"%lotacaoMax);
               

        else:#fim Lotação maxima
            print("Lotação Maxima Atingida Obrigado por Hoje :)\n");
     case "2":
          confirmaSenha=input("Confirma Senha:");
          if confirmaSenha == senha:
             print("$--Caixa Encerrado--$\n");
          else:
             print("Senha Invalida Contantar Administrador\n");
             opcao ="" #limpei a varivel do meu laço para não ecerra quando adm erra senha 
     case _:#outro caso  
          print("[#### OPÇÃO NÃO ENCONTRADA ERRO 404 ######]");

         