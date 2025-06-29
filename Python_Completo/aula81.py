# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas
# que contêm apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.

# Definindo uma lista de dicionários com nomes e sobrenomes.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},  # Primeiro dicionário.
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},  # Segundo dicionário.
    {'nome': 'Daniel', 'sobrenome': 'Silva'},  # Terceiro dicionário.
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},  # Quarto dicionário.
    {'nome': 'Aline', 'sobrenome': 'Souza'},  # Quinto dicionário.
]

# Função que exibe os elementos de uma lista.
def exibir(lista):
    for item in lista:  # Itera sobre cada item da lista.
        print(item)  # Imprime o item atual.
    print()  # Imprime uma linha em branco para separação.

"""
A função 'exibir' recebe uma lista como argumento e imprime cada dicionário contido na lista.
No final, imprime uma linha em branco para melhor formatação da saída.
"""

# Ordena a lista de dicionários pela chave 'nome' usando uma função lambda.
l1 = sorted(lista, key=lambda item: item['nome'])

"""
A função 'sorted' retorna uma nova lista ordenada.
A função lambda 'lambda item: item['nome']' é usada como chave de ordenação,
indicando que a ordenação deve ser feita pelo valor associado à chave 'nome' de cada dicionário.
"""

# Ordena a lista de dicionários pela chave 'sobrenome' usando uma função lambda.
l2 = sorted(lista, key=lambda item: item['sobrenome'])

"""
Da mesma forma, a função 'sorted' é usada novamente para criar uma nova lista ordenada.
Desta vez, a função lambda 'lambda item: item['sobrenome']' é usada como chave de ordenação,
indicando que a ordenação deve ser feita pelo valor associado à chave 'sobrenome' de cada dicionário.
"""

# Exibe a lista ordenada por nome.
exibir(l1)

# Exibe a lista ordenada por sobrenome.
exibir(l2)

"""
As listas ordenadas 'l1' e 'l2' são passadas para a função 'exibir',
que imprime os elementos de cada lista.
"""
 