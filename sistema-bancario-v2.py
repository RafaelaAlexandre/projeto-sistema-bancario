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