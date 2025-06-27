# ================= SISTEMA BANCÁRIO SIMPLES =================
# Esse programa simula um caixa eletrônico com depósito, saque e extrato.

# Menu de opções que será exibido para o usuário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

# ================= VARIÁVEIS INICIAIS =================
saldo = 0                      # Saldo da conta bancária
limite = 500                  # Limite máximo por saque
extrato = ""                  # Histórico das movimentações
numero_saques = 0             # Contador de saques realizados
LIMITE_SAQUES = 3             # Máximo de saques por sessão

# ================= LAÇO PRINCIPAL =================
while True:
    opcao = input(menu)  # Exibe o menu e recebe a opção do usuário

    # ---------- DEPÓSITO ----------
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor  # Atualiza o saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")

    # ---------- SAQUE ----------
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor  # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra no extrato
            numero_saques += 1  # Incrementa o número de saques
        else:
            print("Operação falhou! O valor informado é inválido.")

    # ---------- EXTRATO ----------
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # ---------- SAIR ----------
    elif opcao == "q":
        break  # Encerra o loop e finaliza o programa

    # ---------- OPÇÃO INVÁLIDA ----------
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
