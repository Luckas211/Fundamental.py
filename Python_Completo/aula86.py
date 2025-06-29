# Dictionary Comprehension e Set Comprehension

# Definindo um dicionário com informações de um produto
produto = {
    'nome': 'Caneta Azul',  # Nome do produto
    'preco': 2.5,  # Preço do produto
    'categoria': 'Escritório',  # Categoria do produto
}
"""Dicionário 'produto' que contém informações sobre um item com chaves 'nome', 'preco' e 'categoria'"""

# Dictionary comprehension para criar um novo dicionário
dc = {  # Inicia a dictionary comprehension
    chave: valor.upper()  # Converte o valor para maiúsculas se for uma string
    if isinstance(valor, str) else valor  # Verifica se o valor é uma string
    for chave, valor in produto.items()  # Itera sobre cada par chave-valor no dicionário produto
    if chave != 'categoria'  # Exclui o par chave-valor onde a chave é 'categoria'
}  # Finaliza a dictionary comprehension
"""Cria um novo dicionário 'dc' com os valores convertidos para maiúsculas se forem strings, excluindo a chave 'categoria'"""

# Definindo uma lista de tuplas
lista = [
    ('a', 'valor a'),  # Primeira tupla
    ('b', 'valor a'),  # Segunda tupla (duplicada)
    ('b', 'valor a'),  # Terceira tupla (duplicada)
]
"""Lista de tuplas 'lista' com chaves e valores"""

# Dictionary comprehension para criar um dicionário a partir de uma lista de tuplas
dc = {  # Inicia a dictionary comprehension
    chave: valor  # Usa chave e valor diretamente das tuplas
    for chave, valor in lista  # Itera sobre cada tupla na lista
}  # Finaliza a dictionary comprehension
"""Cria um novo dicionário 'dc' a partir da lista de tuplas. Se houver chaves duplicadas, a última ocorrência prevalece"""

# Set comprehension para criar um conjunto de potências de 2
s1 = {  # Inicia a set comprehension
    2 ** i  # Calcula 2 elevado à potência de i
    for i in range(10)  # Itera sobre os números de 0 a 9
}  # Finaliza a set comprehension
"""Cria um conjunto 's1' contendo as potências de 2 de 0 a 9"""

# Imprime o conjunto resultante
print(s1)  # Imprime o conjunto de potências de 2
"""Imprime o conjunto 's1', que contém os valores {1, 2, 4, 8, 16, 32, 64, 128, 256, 512}"""
