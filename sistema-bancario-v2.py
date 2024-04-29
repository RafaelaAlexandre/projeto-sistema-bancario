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
def deposito(valor, saldo, extrato):
   if valor > 0:
      saldo+=valor
      extrato+= f"Deposito: R$ {valor:.2f}\n"
      return True, saldo, extrato
   else:
      return False, saldo, extrato