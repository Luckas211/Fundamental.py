# Exemplo básico sem list comprehension
lista = []  # Cria uma lista vazia
"""Cria uma lista vazia para armazenar tuplas de coordenadas (x, y)"""

for x in range(3):  # Itera sobre os números de 0 a 2
    """Inicia um loop para iterar sobre x de 0 a 2"""
    for y in range(3):  # Itera sobre os números de 0 a 2 para cada x
        """Inicia um loop aninhado para iterar sobre y de 0 a 2"""
        lista.append((x, y))  # Adiciona a tupla (x, y) à lista
        """Adiciona a tupla (x, y) à lista"""

# List comprehension equivalente ao código acima
lista = [  # Inicia uma list comprehension
    (x, y)  # Cria uma tupla (x, y)
    for x in range(3)  # Itera sobre os números de 0 a 2
    for y in range(3)  # Itera sobre os números de 0 a 2 para cada x
]  # Finaliza a list comprehension
"""Cria uma lista de tuplas (x, y) onde x e y variam de 0 a 2"""

# List comprehension com tuplas de coordenadas e letras
lista = [  # Inicia uma list comprehension
    [(x, letra) for letra in 'Luiz']  # Cria uma lista de tuplas (x, letra) para cada letra em 'Luiz'
    for x in range(3)  # Itera sobre os números de 0 a 2
]  # Finaliza a list comprehension
"""Cria uma lista de listas onde cada sub-lista contém tuplas (x, letra) com x variando de 0 a 2 e letra variando sobre 'Luiz'"""

print(lista)  # Imprime a lista resultante
"""Imprime a lista de listas de tuplas geradas"""
