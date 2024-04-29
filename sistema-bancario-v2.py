def menu_operacao():
   menu = """

   Escolha a operação desejada:

   [1] DEPOSITO
   [2] SAQUE
   [3] EXTRATO
   [0] SAIR

   """ 
   return int(input(menu+"==>"))
def menu_cliente():
   menu = """

    Escolha a operação desejada:

    [1] CADASTRAR CLIENTE
    [2] LISTAR CLIENTES
    [3] CADASTRAR CONTA 
    [4] LISTAR CONTA
    [5] ACESSAR CONTA
    [0] SAIR

    """ 
   return int(input(menu+"==>"))
def deposito(valor, saldo, extrato,/):
   if valor > 0:
      saldo+=valor
      extrato+= f"Deposito: R$ {valor:.2f}\n"
      return True, saldo, extrato
   else:
      return False, saldo, extrato
def saque(*,valor, saldo, extrato, limite_valor, limite_quant, quant):
   if quant < limite_quant:
      if valor <= saldo:    
         if valor <= limite_valor:
            saldo-=valor
            extrato+= f"Saque: R$ {valor:.2f}\n"
            quant+=1
            print(quant)
            return True, saldo, extrato, quant
         else:
            return False, saldo, extrato, quant
      else:
         return False, saldo, extrato, quant
   else:
      return False, saldo, extrato, quant
def extrato(saldo,/,*,extrato):
   if extrato != "" :
      extrato+= f"saldo total: R$ {saldo:.2f}"
      return True, extrato
   else:
      return False, extrato
def nova_conta(agencia, num_conta, usuario, contas_corrente):
   novo_dicionario = {'agencia': agencia, 'num_conta': num_conta, 'usuario': usuario, 'saldo':0, 'extrato':"",'quant':0 }
   contas_corrente.append(novo_dicionario)
   num_conta += 1
   return num_conta 
def novo_cliente(nome, data_nasc, cpf, endereco, clientes):
   novo_dicionario = {'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco':endereco}
   clientes.append(novo_dicionario)
def exibir_clientes(clientes):
   for dicionario in clientes:
        print("nome:", dicionario['nome'])
        print("data de nascimento:", dicionario['data_nasc'])
        print("cpf:", dicionario['cpf'])
        print("endereço:", dicionario['endereco'])
def buscar_cliente(Clientes, cpf):
   for i in Clientes:
      if i['cpf']==cpf:
         return True
   return False
def exibir_contas(contas):
    for conta in contas:
        print("Agência:", conta['agencia'])
        print("Número da Conta:", conta['num_conta'])
        print("Usuário:", conta['usuario'])
        print("Saldo:", conta['saldo'])
        print("Extrato:", conta['extrato'])
        print()
def buscar_conta(lista_contas, num_conta):
    for conta in lista_contas:
        if conta['num_conta'] == num_conta:
            return conta
    return None
lista_clientes=[]
lista_contas=[]
LIMITE_VALOR=500
LIMITE_QUANT=3
num_conta=1


while True:
   opcao=menu_cliente()

   if opcao == 1:
      nome=input("entre com o nome:")
      data_nasc=input("entre com a data no formato xx/xx/xxxx")
      cpf=int(input("entre com cpf [apenas numeros]:"))
      endereco=input("entre com o endereço")
      if buscar_cliente(lista_clientes, cpf) == False:
         novo_cliente(nome, data_nasc, cpf, endereco, lista_clientes)
      else:
         print("cliente ja existente") 

   elif opcao == 2:
      exibir_clientes(lista_clientes)

   elif opcao == 3:
      usuario=int(input("entre com cpf [apenas numeros]:"))
      if buscar_cliente(lista_clientes, usuario) == True:
         num_conta= nova_conta( "0001" , num_conta, usuario, lista_contas)
      else:
         print("cliente não existente") 

   elif opcao == 4:
      exibir_contas(lista_contas)

   elif opcao == 5:
      numero = int(input("qual a conta deseja acessar:"))
      conta= buscar_conta(lista_contas, numero)
      if  conta != None: 
         while True:
            operacao= menu_operacao()
            if operacao == 1:
               valor=int(input("Qual valor deseja depositar"))
               validador, conta['saldo'], conta['extrato'] = deposito(valor, conta['saldo'], conta['extrato'])
               if validador == True:
                  print("Deposito realizado com sucesso")
               else:
                  print("Deposito não realizado")
            elif operacao == 2:
               valor=int(input("Qual valor deseja Sacar"))
               validador, conta['saldo'], conta['extrato'], conta['quant'] = saque(valor=valor, saldo=conta['saldo'], extrato=conta['extrato'], limite_valor=LIMITE_VALOR, limite_quant=LIMITE_QUANT, quant=conta['quant'])
               if validador == True:
                  print("Saque realizado com sucesso")
               else:
                  print("Saque não realizado")
            elif operacao == 3:
               Validador, Extrato = extrato (conta['saldo'],extrato=conta['extrato'])
               if Validador == True:
                  print(Extrato)
               else:
                  print("Nunhuma transação realizada!")
            elif operacao == 0:
               break
            else:
               print("Operação invalida!!") 
      else:
         print("conta não existe")   

   elif opcao == 0:
      break

   else:
      print("Opção inválida!!")