menu = """

    BEM VINDO AO SISTEMA BANCARIO

    Escolha a operação desejada:

    [1] DEPOSITO
    [2] SAQUE
    [3] EXTRATO
    [0] SAIR

"""

LIMITE_VALOR_SAQUE=500.00
LIMITE_QUANT_SAQUE=3
quant=0
saldo=0
extrato=""

while True:
    opcao=int(input(menu+"==>>"))

    if opcao == 1:
        print("Voce escolheu a opção: DEPOSITO")
        deposito=float(input("entre com o valor que deseja depositar: "))
        if deposito > 0:
            saldo+=deposito
            extrato+= f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("valor inválido para deposito")   
    elif opcao == 2:
        print("Voce escolheu a opção: SAQUE")
    elif opcao == 3:
        print("Voce escolheu a opção: EXTRATO")
    elif opcao == 0:
        print("Voce escolheu a opção: SAIR")
        break
    else:
        print("Opção inválida!")            