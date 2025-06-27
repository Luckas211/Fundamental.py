menu = "[D] DEPOSITAR, [S] SACAR, [E] EXTRATO, [Q] SAIR: "

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    alternativa = input(menu)

    if alternativa == "D":
        valor = float(input("Quanto você deseja depositar?: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é incorreto!")



    elif alternativa == "S":
        print("Sacar")
    elif alternativa == "E":
        print("Extrato")
    elif alternativa == "Q":
        break
    else:
        print("Não existe essa alternativa")
