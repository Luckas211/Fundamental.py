a,b =1,2
a,b = b,a

print(a,b)
print("-= "*20)
pessoas = {"Nome": "Lucas", "Sobrenome":"Silva"}
c,d = pessoas
print(c,d)
print("-= "*20)
(a1,a2),(b1,b2) = pessoas.items()
print(a1,a2,"---",b1,b2)
print(a2,b2)


print("-= "*20)
valores1, valores2 = pessoas.values()
print("ESSES SÃO OS VALUES! ",valores1,valores2)
print("-= "*20)

item1,item2 = pessoas.items()
print("ESSES SÃO OS ITEMS! ",item1,item2)
print("-= "*20)
key1,key2 = pessoas.keys()
print("ISSO SÃO AS KEYS ",key1,key2)
print("-= "*20)

for chave, valor in pessoas.items():
    print("chave:",chave,"--""valor:",valor)
print()
print()


# Exemplo de uso de *args e **kwargs

# Definindo uma função que recebe argumentos nomeados
def saudacao(**kwargs):
    print("Argumentos Nomeados:")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Definindo uma função que recebe argumentos não nomeados
def lista_itens(*args):
    print("Argumentos Não Nomeados:")
    for item in args:
        print(item)

# Chamando a função de saudação com argumentos nomeados
saudacao(nome="João", idade=30, cidade="São Paulo")

# Chamando a função de lista_itens com argumentos não nomeados
lista_itens("maçã", "banana", "laranja", "morango")
