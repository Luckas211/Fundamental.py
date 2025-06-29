# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

import pprint  # Importa o módulo pprint para impressão formatada
"""Importa o módulo pprint para permitir a impressão formatada de estruturas de dados"""

def p(v):  # Define uma função de impressão formatada
    pprint.pprint(v, sort_dicts=False, width=40)
"""Define uma função chamada 'p' que utiliza pprint para imprimir dados de forma mais legível"""

# Exemplo básico sem list comprehension
lista = []  # Cria uma lista vazia
"""Cria uma lista vazia para armazenar os números de 0 a 9"""

for numero in range(10):  # Itera sobre os números de 0 a 9
    """Inicia um loop que vai de 0 a 9"""
    lista.append(numero)  # Adiciona cada número à lista
    """Adiciona cada número iterado à lista"""

# print(lista)  # Imprime a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""Descomente a linha acima para imprimir a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""

# Exemplo usando list comprehension
lista = [  # Inicia uma list comprehension
    numero * 2  # Multiplica cada número por 2
    for numero in range(10)  # Itera sobre os números de 0 a 9
]  # Finaliza a list comprehension
"""Cria uma nova lista onde cada número de 0 a 9 é multiplicado por 2"""

# print(list(range(10)))  # Imprime a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""Descomente a linha acima para imprimir a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
# print(lista)  # Imprime a lista [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
"""Descomente a linha acima para imprimir a lista [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]"""

# Mapeamento de dados em list comprehension
produtos = [  # Cria uma lista de produtos, cada um representado por um dicionário
    {'nome': 'p1', 'preco': 20},  # Primeiro produto
    
    {'nome': 'p2', 'preco': 10},  # Segundo produto
    
    {'nome': 'p3', 'preco': 30},  # Terceiro produto    
]  # Finaliza a lista de produtos
"""Cria uma lista de dicionários, cada um representando um produto com nome e preço"""

novos_produtos = [  # Inicia uma list comprehension para criar uma nova lista de produtos
    {**produto, 'preco': produto['preco'] * 1.05}  # Aumenta o preço em 5% se for maior que 20
    if produto['preco'] > 20 else {**produto}  # Mantém o preço se for 20 ou menor
    for produto in produtos  # Itera sobre cada produto na lista
]  # Finaliza a list comprehension
"""Cria uma nova lista de produtos onde os preços maiores que 20 são aumentados em 5%"""

# print(novos_produtos)  # Imprime a nova lista de produtos com preços ajustados
"""Descomente a linha acima para imprimir a nova lista de produtos com preços ajustados"""
# p(novos_produtos)  # Imprime a nova lista de produtos com preços ajustados usando pprint
"""Descomente a linha acima para imprimir a nova lista de produtos com preços ajustados usando pprint"""

# Filtragem em list comprehension
novos_produtos = [  
    
    {**produto, 'preco': produto['preco'] * 1.05}  # Aumenta o preço em 5% se for maior que 20
   
    if produto['preco'] > 20 else {**produto}  # Mantém o preço se for 20 ou menor
    
    for produto in produtos  # Itera sobre cada produto na lista
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10  # Filtra os produtos para incluir apenas aqueles com preço ajustado > 10
]  # Finaliza a list comprehension
"""Cria uma nova lista de produtos onde os preços maiores que 20 são aumentados em 5% e inclui apenas produtos cujo preço ajustado é maior que 10"""

p(novos_produtos)  # Imprime a nova lista de produtos filtrados e ajustados usando pprint
"""Imprime a nova lista de produtos filtrados e ajustados usando pprint"""








'''

# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de iteráveis.

import pprint  # Importa o módulo pprint para impressão formatada
"""Importa o módulo pprint para permitir a impressão formatada de estruturas de dados"""

def p(v):  # Define uma função de impressão formatada
    pprint.pprint(v, sort_dicts=False, width=40)
"""Define uma função chamada 'p' que utiliza pprint para imprimir dados de forma mais legível"""

# Exemplo básico sem list comprehension
lista = []  # Cria uma lista vazia
"""Cria uma lista vazia para armazenar os números de 0 a 9"""

for numero in range(10):  # Itera sobre os números de 0 a 9
    """Inicia um loop que vai de 0 a 9"""
    lista.append(numero)  # Adiciona cada número à lista
    """Adiciona cada número iterado à lista"""

# print(lista)  # Imprime a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""Descomente a linha acima para imprimir a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""

# Exemplo usando list comprehension
lista = [  # Inicia uma list comprehension
    numero * 2  # Multiplica cada número por 2
    for numero in range(10)  # Itera sobre os números de 0 a 9
]  # Finaliza a list comprehension
"""Cria uma nova lista onde cada número de 0 a 9 é multiplicado por 2"""

# print(list(range(10)))  # Imprime a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""Descomente a linha acima para imprimir a lista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
# print(lista)  # Imprime a lista [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
"""Descomente a linha acima para imprimir a lista [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]"""

# Mapeamento de dados em list comprehension
produtos = [  # Cria uma lista de produtos, cada um representado por um dicionário
    {'nome': 'p1', 'preco': 20},  # Primeiro produto
    """Dicionário representando o primeiro produto com nome 'p1' e preço 20"""
    {'nome': 'p2', 'preco': 10},  # Segundo produto
    """Dicionário representando o segundo produto com nome 'p2' e preço 10"""
    {'nome': 'p3', 'preco': 30},  # Terceiro produto
    """Dicionário representando o terceiro produto com nome 'p3' e preço 30"""
]  # Finaliza a lista de produtos
"""Cria uma lista de dicionários, cada um representando um produto com nome e preço"""

novos_produtos = [  # Inicia uma list comprehension para criar uma nova lista de produtos
    {**produto, 'preco': produto['preco'] * 1.05}  # Aumenta o preço em 5% se for maior que 20
    """Desempacota o dicionário do produto e atualiza o preço multiplicando por 1.05"""
    if produto['preco'] > 20 else {**produto}  # Mantém o preço se for 20 ou menor
    """Mantém o produto inalterado se o preço for 20 ou menor"""
    for produto in produtos  # Itera sobre cada produto na lista
]  # Finaliza a list comprehension
"""Cria uma nova lista de produtos onde os preços maiores que 20 são aumentados em 5%"""

# print(novos_produtos)  # Imprime a nova lista de produtos com preços ajustados
"""Descomente a linha acima para imprimir a nova lista de produtos com preços ajustados"""
# p(novos_produtos)  # Imprime a nova lista de produtos com preços ajustados usando pprint
"""Descomente a linha acima para imprimir a nova lista de produtos com preços ajustados usando pprint"""

# Filtragem em list comprehension
novos_produtos = [  # Inicia uma list comprehension para criar uma nova lista de produtos filtrados e atualizados
    {**produto, 'preco': produto['preco'] * 1.05}  # Aumenta o preço em 5% se for maior que 20
    """Desempacota o dicionário do produto e atualiza o preço multiplicando por 1.05"""
    if produto['preco'] > 20 else {**produto}  # Mantém o preço se for 20 ou menor
    """Mantém o produto inalterado se o preço for 20 ou menor"""
    for produto in produtos  # Itera sobre cada produto na lista
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10  # Filtra os produtos para incluir apenas aqueles com preço ajustado > 10
]  # Finaliza a list comprehension
"""Cria uma nova lista de produtos onde os preços maiores que 20 são aumentados em 5% e inclui apenas produtos cujo preço ajustado é maior que 10"""

p(novos_produtos)  # Imprime a nova lista de produtos filtrados e ajustados usando pprint
"""Imprime a nova lista de produtos filtrados e ajustados usando pprint"""




'''
