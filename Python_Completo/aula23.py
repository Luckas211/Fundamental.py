# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
print(not True)  # False
print(not False)  # True

senha = input("senha: ")

if not senha:
    print("Você não digitou nada")


print(not 0)