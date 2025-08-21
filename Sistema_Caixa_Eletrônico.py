menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 200
limite = 1000
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_saque = numero_de_saques >= LIMITE_SAQUES

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif execedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        elif execedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n=======EXTRATO===========")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")

    elif opcao == "4":
        print("Obraigado por Utilizar nosso banco.")
        break



    else:
        print("Operação inválida! Tente novamente.")
