import os #importando bibiotleca para cls

#Variaveis supostamente declaradas 
funcionario:str;
kids:float;
adultos:float;
jovens:float;
universitystudent:float;
lotacaoMax:int;
idade:int;
senha:str;
contLotacao:int;
contLotacao=0;
dinheiro:float;
troco:float
#menu inicial
print("\n[#############Adiministrado do Cuca#############]\n");
print("Infomer Capacidade Máxima do Dia: ",end="");#
lotacaoMax = int(input());
senha=input("Crie um senha para o dia: ");

  
os.system("cls") #limpa tela 

opcao =""
while opcao!= "2": #laço principal de repetição do menu
    print("-----------==[Entradas Visitante]==-----------");
    print("[1]Vender>");
    print("[2]Encerra>\n");
    opcao =input(">")
    os.system("cls") 

    match opcao:
     case "1":
        if contLotacao <= lotacaoMax:#!!!!!!!!!!!!!inicio!!!!!!!!!!!!!!!!!!!!!!!!
           print("Idade do visitante: ",end="");
           idade = int(input());

           if idade >=1 and idade <=9:#Criança///////////CRIANÇA///////////////    
              #não precisa de operção finaceria free
              print("INGRESSO VENDIDO");
              print("Categoria:Kids");
              print("Valor:R$ 0.00\n");
              contLotacao+=1;
              kids+=1
              print("ingressos vendidos:%d"%contLotacao);
              print("Capacidade local:%d"%lotacaoMax);#///////CRIANÇA///////////
           
           elif idade >=10 and idade <=17:#//////////ADOLECENTE//////////////////  
              #opreçãofinceira
              pagamento=float(input("Digite o valor pago $:"));
              if pagamento >= 15.00:#validação pagamento menores que valor do ingresso
               troco = pagamento-15.00;
               print("INGRESSO VENDIDO");
               print("Categoria:Adolecente");
               print("Valor:R$ 15,00");
               print("troco R$:%.2f"%troco);
               contLotacao+=1
               dinheiro+=15.00;
               jovens+=15.00
               #informativos
               print("\ningressos vendidos:%d"%contLotacao);
               print("Capacidade local:%d"%lotacaoMax);
              else:
                 print("Pagamento insuficiente!");#//////ADOLECENTE///////////////
              
           elif idade >=18:#//////////////ADULTO//////////////////////////
              print("Estudande Universitario Uefs:"); 
              uefs=int(input("[1]sim----[2]Não \n"));
              os.system("cls");

              if (uefs == 1):#aqui verifico se é estudante
                 matricula=input("Matricula:");#se sim aqui vem a matricula

                 if len(matricula) == 9 and matricula.isdigit():#aqui vejo requisitos matricula
                  pagamento=float(input("Digite o valor pago $:"));
                  if pagamento >=20:#aqui ainda verifico o valrdo pagamento
                   troco =pagamento -20;
                   print("INGRESSSO VENDIDO");
                   print("Categoria:Estudante");
                   print("Valor:R$ 20.00\n");  
                   print("Troco:R$ %.2f"%troco);
                   contLotacao+=1
                   dinheiro+=20.00;
                   universitystudent+=20.00
                   print("\ningressos vendidos:%d"%contLotacao);
                   print("Capacidade local:%d"%lotacaoMax);
                  else:
                      print("Pagamento insuficiente!")##########estudante############
                 else:
                  print("Matricula invalida");#aqui ainda indico se matricula foi errada
                  
              else:#fim controle estudande
                 pagamento=float(input("Digite o valor pago $:"));
                 if pagamento >= 40.00:#validação pagamento menores que valor do 
                  troco = pagamento-40.00;
                  print("INGRESSO VENDIDO");
                  print("Categoria:Adulto");
                  print("Valor:R$ 40.00");
                  print("troco R$:%.2f"%troco);
                  contLotacao+=1;
                  dinheiro+=40.00;
                  adultos+=40.00
                  print("\ningressos vendidos:%d"%contLotacao);
                  print("Capacidade local:%d"%lotacaoMax);
               #//////////////////////ADULTO////////////////////////////

        else:#fim Lotação maxima !!!!!!!!!!!!!!!!!!fechamneto!!!!!!!!!!!!!!!!!!!!!!
            print("Lotação Maxima Atingida Obrigado por Hoje :)\n");
     case "2":
          confirmaSenha=input("Confirma Senha:");
          if confirmaSenha == senha:
             print("$--Caixa Encerrado--$\n");
          else:
             print("Senha Invalida Contantar Administrador\n");
             print("Tente Novamente")
             opcao ="" #limpei a varivel do meu laço para não ecerra quando adm erra senha 
     case _:#outro caso  
          print("[Valor inválido. Insira um número válido]");

    #premiação

    if dinheiro <=300.00:  
        print("\o/ Premiaçoes do DIa \o/");
        premiacao = dinheiro*0.10;
        valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
        print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n 3 lugar R$:%.2f"%(valor1,valor2,valor3));
    if dinheiro >=300.01 and dinheiro <=700.00:  
         print("\o/ Premiaçoes do DIa \o/");
         premiacao = dinheiro*0.10;
         valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
         print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n 3 lugar R$:%.2f"%(valor1,valor2,valor3));
    if dinheiro >=700.00:  
         print("\o/ Premiaçoes do DIa \o/");
         premiacao = dinheiro*0.10;
         valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
         print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n 3 lugar R$:%.2f"%(valor1,valor2,valor3));
    
    


         