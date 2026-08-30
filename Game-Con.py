import os #importando bibiotleca para cls

#Variaveis supostamente declaradas 
funcionario:str;
kids=0;
adultos=0.0;
jovens=0.0;
universitystudent=0.0;
lotacaoMax=0;
idade:int;
senha:str;
contLotacao:int;
contLotacao=0;
dinheiro=0.0;
troco:float
quantJovens=0;
quantAdultos=0;
quantEstudantes=0;
#menu inicial
print("\n[      Adiministrado do Cuca     ]\n");
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
        if contLotacao < lotacaoMax:#!!!!!!!!!!!!!inicio!!!!!!!!!!!!!!!!!!!!!!!!
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
              print("\nCATEGORIA:JOVENS:PREÇO:R$15,00\n");
              pagamento=float(input("Digite o valor pago $:").replace(",","."));
              if pagamento >= 15.00:#validação pagamento menores que valor do ingresso
               troco = pagamento-15.00;
               print("\nINGRESSO VENDIDO");
               print("Categoria:Adolecente");
               print("Valor:R$ 15,00");
               print("troco R$:%.2f"%troco);
               quantJovens+=1;
               contLotacao+=1
               dinheiro+=15.00;
               jovens+=15.00;
               #informativos
               print("\ningressos vendidos:%d"%contLotacao);
               print("Capacidade local:%d"%lotacaoMax);
              else:
                 print("Pagamento insuficiente!");#//////ADOLECENTE///////////////
                  
           elif idade >=18:#//////////////ADULTO//////////////////////////
              uefs ="";
              while uefs != "1" and uefs != "2":
               print("Desconto Estudantil para Universitario Uefs %:"); 
               uefs=input("\n[1]=sim % Não=[2] ");
               input("\nPressione ENTER para confirmar....");
               os.system("cls")
               match uefs:
                case "1":#se for estudante
                 matricula=input("Matricula: ");#se sim aqui vem a matricula

                 if len(matricula) == 9 and matricula.isdigit():#aqui vejo requisitos matricula
                  print("\nCATEGORIA:ESTUDANTE:PREÇO:R$20,00\n");
                  pagamento=float(input("Digite o valor pago $: "));
                  if pagamento >=20:#aqui ainda verifico o valordo pagamento
                   troco =pagamento -20;
                   print("\nINGRESSSO VENDIDO");
                   print("Categoria:Estudante");
                   print("Valor:R$ 20.00\n");  
                   print("Troco:R$ %.2f"%troco);
                   quantEstudantes+=1
                   contLotacao+=1
                   dinheiro+=20.00;
                   universitystudent+=20.00
                   print("\ningressos vendidos:%d"%contLotacao);
                   print("Capacidade local:%d"%lotacaoMax);
                  else:
                      print("Pagamento insuficiente!");##########estudante############
                 else:
                  print("Matricula invalida");#aqui ainda indico se matricula foi errada
                  
                case"2":#se não for estudande
                 print("\nCATEGORIA:ADULTO:PREÇO:R$40,00\n");
                 pagamento=float(input("Digite o valor pago $:"));
                 if pagamento >= 40.00:#validação pagamento menores que valor do 
                  troco = pagamento-40.00;
                  print("\nINGRESSO VENDIDO");
                  print("Categoria:Adulto");
                  print("Valor:R$ 40.00");
                  print("troco R$:%.2f"%troco);
                  quantAdultos+=1;
                  contLotacao+=1;
                  dinheiro+=40.00;
                  adultos+=40.00;
                  print("\ningressos vendidos:%d"%contLotacao);
                  print("Capacidade local:%d"%lotacaoMax);
               #//////////////////////ADULTO////////////////////////////
                case _:
                  print("Valor inválido. Insira um número válido");

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
   print("Premiaçoes do DIa ");
   premiacao = dinheiro*0.10;
   valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
   print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n 3 lugar R$:%.2f"%(valor1,valor2,valor3));
if dinheiro >=300.01 and dinheiro <=700.00:  
   print("\o/ Premiaçoes do DIa \o/");
   premiacao = dinheiro*0.15;
   valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
   print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n 3 lugar R$:%.2f"%(valor1,valor2,valor3));
if dinheiro >=700.00:  
   print("\o/ Premiaçoes do DIa \o/");
   premiacao = dinheiro*0.20;
   valor1 =premiacao*0.50;valor2=premiacao*0.30;valor3=premiacao*0.20
   print("1 lugar R$:%.2f\n2 lugar R$:%.2f\n 3 lugar R$:%.2f"%(valor1,valor2,valor3));
    
    
input("\nPressione ENTER para >>>DETALHES DO CAIXA$<<<<")
os.system("cls")
print("$-----$--$-----$--[Relatorio]--$-----$--$-----$")
print("\nDetalhamento Caixa");

print("\nValores por Categoria");
print("Jovens R$:%.2f.........."%jovens);
print("Adultos R$:%.2f........."%adultos);
print("Estudantes Uefs R$:%.2f.."%universitystudent)
print("Não Pagantes crianças:%d........."%kids);

print("\nIngressos vendido por Categoria")
print("Criança %d"%kids);
print("Jovens %d"%quantJovens);
print("Adultos %d"%quantAdultos);
print("Estudantes %d"%quantEstudantes)

print("\n\nTotal de Pagantes %d"%contLotacao);
print("Média de pagantes R$:%.2f"%(dinheiro/contLotacao));
print("Total do dia R$:%.2f"%dinheiro);


         