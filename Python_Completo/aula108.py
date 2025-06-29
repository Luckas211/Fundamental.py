'''

lista_a = [1,2,3,4,5,6,7]
lista_b = [2,3,4,5]
lista_soma = []

for i in range (len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)
print("Método2")


lista1 = [1,2,3,4,5,6,7,8]
lista2 = [2,3,4,5,6]
resultado = [x + y for x,y in zip(lista1,lista2)]
print(resultado)
print("Divisão de exemplos")

print(list(zip(lista1,lista2)))


print("Métodos com o maior valor")
from itertools import zip_longest
 
lista_a1 = [10, 2, 3, 4, 5]
lista_b2 = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a1, lista_b2, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

Exercício solucionado - somando listas
No exercício anterior, fizemos a soma de duas listas usando várias soluções diferentes.

Uma delas foi usando zip para unir duas listas e utilizar list comprehension para fazer a conta:

lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)  # Saída: [22, 4, 6, 10, 55]
O problema é que zip só une as listas até o tamanho da menor lista (como proposto no exercício).

Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.

A ideia é a mesma, veja:

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]
Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.'''


# Definindo duas listas de números inteiros
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [2, 3, 4, 5]
lista_soma = []

# Itera até o tamanho da lista_b, somando os elementos correspondentes de lista_a e lista_b
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])

# Imprime o resultado da soma dos elementos de lista_a e lista_b
print(lista_soma)  # Saída: [3, 5, 7, 9]
print("Método 2")

# Usando list comprehension com zip para somar os elementos correspondentes de duas listas
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [2, 3, 4, 5, 6]
resultado = [x + y for x, y in zip(lista1, lista2)]

# Imprime o resultado da soma dos elementos de lista1 e lista2
print(resultado)  # Saída: [3, 5, 7, 9, 11]
print("Divisão de exemplos")

# Mostra as listas emparelhadas como tuplas usando zip
print(list(zip(lista1, lista2)))  # Saída: [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

print("Métodos com o maior valor")

# Importando zip_longest do módulo itertools para lidar com listas de tamanhos diferentes
from itertools import zip_longest

# Definindo duas novas listas com tamanhos diferentes
lista_a1 = [10, 2, 3, 4, 5]
lista_b2 = [12, 2, 3, 6, 50, 60, 70]

# Usando zip_longest para somar os elementos das listas, preenchendo os valores faltantes com 0
lista_soma = [x + y for x, y in zip_longest(lista_a1, lista_b2, fillvalue=0)]

# Imprime o resultado da soma, que inclui todos os elementos de ambas as listas
print(lista_soma)  # Saída: [22, 4, 6, 10, 55, 60, 70]