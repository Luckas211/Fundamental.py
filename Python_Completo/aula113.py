# reduce - faz a redução de um iterável em um valor único
from functools import reduce  # Importa a função reduce do módulo functools

# Uma lista de produtos, cada produto é representado como um dicionário com 'nome' e 'preco'
produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# Exemplo comentado de uma função regular que poderia ser usada com reduce.
# Ela seria chamada em cada iteração do reduce para acumular o valor total dos preços.
# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)  # Mostra o valor atual do acumulador
#     print('produto', produto)  # Mostra o produto atual que está sendo processado
#     print()
#     return acumulador + produto['preco']  # Adiciona o preço do produto ao acumulador

# Usando a função reduce para somar todos os preços dos produtos
total = reduce(
    # Lambda que soma o valor acumulado (ac) ao preço do produto atual (p)
    lambda ac, p: ac + p['preco'],
    produtos,  # Iterável sobre o qual a redução será aplicada (nossa lista de produtos)
    0  # Valor inicial do acumulador (começa a soma a partir de 0)
    
)
for i in produtos:
    print(i["preco"])

print('Total é', total)  # Exibe o valor total calculado

# Alternativa comentada: usando um loop for clássico para calcular o total
# total = 0
# for p in produtos:
#     total += p['preco']  # Soma o preço de cada produto ao total

# print(total)  # Exibe o total calculado pelo loop for

# Outra alternativa comentada: usando a função sum com list comprehension
# print(sum([p['preco'] for p in produtos]))  # Soma diretamente os preços usando sum
