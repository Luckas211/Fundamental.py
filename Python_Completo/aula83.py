"""
# Empacotamento e desempacotamento de dicionários
"""
a, b = 1, 2  # Define a como 1 e b como 2
a, b = b, a  # Troca os valores de a e b usando desempacotamento
# print(a, b)  # Imprime os valores trocados de a e b

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}  # Combina os dois dicionários em um usando desempacotamento
# print(pessoas_completa)  # Imprime o dicionário resultante da combinação

"""
# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
"""


def mostro_argumentos_nomeados(*args, **kwargs):
    """
    Função que exibe argumentos não nomeados e nomeados.
    """
    print('NÃO NOMEADOS:', args)  # Imprime os argumentos não nomeados

    for chave, valor in kwargs.items():
        print(chave, valor)  # Itera sobre kwargs e imprime cada chave e valor


# mostro_argumentos_nomeados(nome='Joana', qlq=123)  # Chama a função com argumentos nomeados
# mostro_argumentos_nomeados(**pessoas_completa)  # Desempacota o dicionário pessoas_completa e passa como kwargs

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}  # Define um dicionário de configurações
mostro_argumentos_nomeados(**configuracoes)  # Desempacota o dicionário configuracoes e passa como kwargs

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

