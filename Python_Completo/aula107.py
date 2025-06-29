# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
'''from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))'''

from itertools import zip_longest  # Importa a função zip_longest do módulo itertools

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']  # Lista de cidades
l2 = ['BA', 'SP', 'MG', 'RJ']  # Lista de estados

# Combina as listas l1 e l2 pareando os elementos na mesma posição. Como l2 tem um elemento a mais, ele é ignorado.
print(list(zip(l1, l2)))  
# Saída: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Combina as listas l1 e l2 pareando os elementos na mesma posição, mas preenche com 'SEM CIDADE' onde faltar elementos em l1.
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))
# Saída: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG'), ('SEM CIDADE', 'RJ')]