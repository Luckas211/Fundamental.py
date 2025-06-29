# Função auxiliar para imprimir todos os itens de um iterador
def print_iter(iterator):
    """
    Converte o iterador em uma lista e imprime cada elemento em uma nova linha.
    """
    print(*list(iterator), sep='\n')
    print()

# Lista de dicionários contendo produtos, cada um com um nome e um preço
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Função que verifica se o preço de um produto é maior que 100
def filtrar_preco(produto):
    """
    Recebe um dicionário 'produto' e retorna True se o preço for maior que 100, 
    caso contrário, retorna False.
    """
    return produto['preco'] > 100

# Utiliza a função `filter` para filtrar produtos com preço acima de 100
novos_produtos = filter(
    filtrar_preco,  # Função de filtro que será aplicada a cada item
    produtos  # Lista de produtos a ser filtrada
)

# Imprime a lista original de produtos
print_iter(produtos)

# Imprime a lista de produtos filtrados
print_iter(novos_produtos)


