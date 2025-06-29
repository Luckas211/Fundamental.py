# Importando as funções combinations, permutations e product do módulo itertools.
# - combinations: Gera todas as combinações possíveis de um iterável para um tamanho de grupo especificado, sem considerar a ordem.
# - permutations: Gera todas as permutações possíveis (considerando a ordem) de um iterável para um tamanho de grupo especificado.
# - product: Gera o produto cartesiano de iteráveis, considerando todas as combinações possíveis, incluindo repetições de valores únicos.
from itertools import combinations, permutations, product

# Definindo uma função para imprimir os valores de um iterador.
# - A função list() converte o iterador em uma lista.
# - O * (asterisco) é usado para descompactar os elementos da lista, passando-os como argumentos individuais para print.
# - sep='\n' define o separador como uma nova linha, então cada elemento é impresso em uma linha separada.
# - No final, uma linha em branco é impressa para separar as saídas.
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# Definindo uma lista de pessoas.
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

# Definindo uma lista de listas, onde cada lista interna contém atributos diferentes de camisetas.
# As listas internas representam opções de cores, tamanhos, gêneros e materiais, respectivamente.
camisetas = [
    ['preta', 'branca'],  # Cores disponíveis
    ['p', 'm', 'g'],  # Tamanhos disponíveis
    ['masculino', 'feminino', 'unisex'],  # Gêneros disponíveis
    ['algodão', 'poliéster']  # Materiais disponíveis
]

# Gera e imprime todas as combinações de 2 pessoas da lista 'pessoas'.
# - combinations(pessoas, 2) retorna um iterador com todas as combinações possíveis de 2 elementos da lista.
# - A função print_iter é chamada para imprimir essas combinações.
print_iter(combinations(pessoas, 2))

# Gera e imprime todas as permutações de 2 pessoas da lista 'pessoas'.
# - permutations(pessoas, 2) retorna um iterador com todas as permutações possíveis de 2 elementos da lista.
# - A função print_iter é chamada para imprimir essas permutações.
print_iter(permutations(pessoas, 2))

# Gera e imprime o produto cartesiano das listas internas em 'camisetas'.
# - product(*camisetas) retorna um iterador com todas as combinações possíveis de um elemento de cada lista interna em 'camisetas'.
# - O operador * descompacta a lista 'camisetas' em seus elementos individuais, passando-os como argumentos para product.
# - A função print_iter é chamada para imprimir essas combinações.
print_iter(product(*camisetas))