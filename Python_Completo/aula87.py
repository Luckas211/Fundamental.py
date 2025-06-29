# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]
"""Define uma lista com diversos tipos de dados: string, inteiro, float, booleano, lista, tupla, set, e dicionário"""

for item in lista:  # Itera sobre cada item na lista
    """Inicia um loop que percorre cada item da lista"""
    if isinstance(item, set):  # Verifica se o item é do tipo set
        """Verifica se o item atual é um set"""
        print('SET')  # Imprime 'SET' se a condição for verdadeira
        """Imprime 'SET' para indicar que o item é um set"""
        item.add(5)  # Adiciona o valor 5 ao set
        """Adiciona o valor 5 ao set"""
        print(item, isinstance(item, set))  # Imprime o set atualizado e confirma que é um set
        """Imprime o set atualizado e verifica novamente se é um set"""

    elif isinstance(item, str):  # Verifica se o item é do tipo string
        """Verifica se o item atual é uma string"""
        print('STR')  # Imprime 'STR' se a condição for verdadeira
        """Imprime 'STR' para indicar que o item é uma string"""
        print(item.upper())  # Imprime a string em maiúsculas
        """Imprime a string em letras maiúsculas"""

    elif isinstance(item, (int, float)):  # Verifica se o item é do tipo inteiro ou float
        """Verifica se o item atual é um número (inteiro ou float)"""
        print('NUM')  # Imprime 'NUM' se a condição for verdadeira
        """Imprime 'NUM' para indicar que o item é um número"""
        print(item, item * 2)  # Imprime o número e seu dobro
        """Imprime o número atual e o resultado da multiplicação do número por 2"""
    else:  # Se o item não for nenhum dos tipos acima
        """Se o item não for um set, string, inteiro ou float"""
        print('OUTRO')  # Imprime 'OUTRO'
        """Imprime 'OUTRO' para indicar que o item é de um tipo diferente dos anteriores"""
        print(item)  # Imprime o item
        """Imprime o item atual"""
