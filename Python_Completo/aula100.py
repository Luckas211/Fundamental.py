import copy
# Importa o módulo 'copy', que fornece funções para criar cópias superficiais e profundas de objetos.

from dados import produtos
# Importa a lista 'produtos' do módulo 'dados' (esta linha parece ser redundante e pode ser removida já que os produtos são definidos novamente abaixo).

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Define a lista 'produtos' com dicionários representando produtos e seus preços.

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
# Cria uma nova lista 'novos_produtos', onde cada produto é uma cópia profunda (deepcopy) de um produto original,
# com o preço aumentado em 10% e arredondado para duas casas decimais.

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
# Cria uma nova lista 'produtos_ordenados_por_nome', ordenando os produtos originais pelo nome em ordem decrescente,
# usando uma cópia profunda dos produtos originais.

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)
# Cria uma nova lista 'produtos_ordenados_por_preco', ordenando os produtos originais pelo preço em ordem crescente,
# usando uma cópia profunda dos produtos originais.

# FINAL

print(*produtos, sep='\n')
# Imprime todos os produtos originais, cada um em uma nova linha.

print()
# Imprime uma linha em branco para separar as seções.

print(*novos_produtos, sep='\n')
# Imprime todos os novos produtos (com o preço ajustado), cada um em uma nova linha.

print()
# Imprime uma linha em branco para separar as seções.

print(*produtos_ordenados_por_nome, sep='\n')
# Imprime os produtos ordenados por nome, cada um em uma nova linha.

print()
# Imprime uma linha em branco para separar as seções.

print(*produtos_ordenados_por_preco, sep='\n')
# Imprime os produtos ordenados por preço, cada um em uma nova linha.