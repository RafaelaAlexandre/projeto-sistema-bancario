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
   novo_dicionario = {'agencia': agencia, 'num_conta': num_conta, 'usuario': usuario, 'saldo':0, 'extrato':"" }
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

lista_clientes=[]
lista_contas=[]
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
      if buscar_cliente(lista_clientes, usuario) == False:
         num_conta= nova_conta( "0001" , num_conta, usuario, lista_contas)
      else:
         print("cliente não existente")         
   # elif opcao == 4:
   # elif opcao == 5:
   # elif opcao == 0:
   # else: