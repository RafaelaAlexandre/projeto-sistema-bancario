menu = """

    BEM VINDO AO SISTEMA BANCARIO

    Escolha a operação desejada:

    [1] SAQUE
    [2] DEPOSITO
    [3] EXTRATO
    [0] SAIR

"""

while True:
    opcao=int(input(menu+"==>>"))

    if opcao == 1:
        print("Voce escolheu a opção: SAQUE")
    elif opcao == 2:
        print("Voce escolheu a opção: DEPOSITO")
    elif opcao == 3:
        print("Voce escolheu a opção: EXTRATO")
    elif opcao == 0:
        print("Voce escolheu a opção: SAIR")
        break
    else:
        print("Opção inválida!")            