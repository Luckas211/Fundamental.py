# Importando a função count do módulo itertools.
# - count: Gera um iterador que retorna uma sequência infinita de números, começando de um valor inicial e incrementando por um valor de passo definido.
from itertools import count

# Criando um iterador infinito usando count, começando em 8 e com um incremento de 8 a cada iteração.
c1 = count(step=8, start=8)

# Criando um objeto range que gera números de 8 a 55 (não inclusivo), com um incremento de 8.
r1 = range(8, 56, 8)

# Verificando se c1 é um iterador.
# - hasattr(c1, '__iter__') verifica se c1 é iterável, ou seja, se ele pode ser percorrido em um loop.
# - hasattr(c1, '__next__') verifica se c1 é um iterador, ou seja, se ele pode retornar o próximo valor com o método __next__.
print('c1', hasattr(c1, '__iter__'))  # Deve imprimir True, pois c1 é um iterador.
print('c1', hasattr(c1, '__next__'))  # Deve imprimir True, pois c1 pode produzir valores infinitamente.

# Verificando se r1 é um iterador.
# - hasattr(r1, '__iter__') verifica se r1 é iterável.
# - hasattr(r1, '__next__') verifica se r1 é um iterador. (Nota: r1 é iterável, mas não é um iterador).
print('r1', hasattr(r1, '__iter__'))  # Deve imprimir True, pois r1 é iterável.
print('r1', hasattr(r1, '__next__'))  # Deve imprimir False, pois r1 é iterável, mas não um iterador.

# Imprimindo valores gerados por c1 (count).
print('count')
# Itera sobre c1 (o iterador infinito gerado por count).
# - O loop continua indefinidamente até que a condição if i >= 56 seja atend
