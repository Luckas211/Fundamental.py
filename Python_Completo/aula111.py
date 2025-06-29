from functools import partial
"""Importa a função `partial` do módulo `functools`. 
Essa função permite criar uma nova função com alguns argumentos já pré-definidos."""

from types import GeneratorType
"""Importa `GeneratorType` do módulo `types`, que é usado para verificar se um objeto é um gerador. 
Generators são iteradores especiais que produzem valores sob demanda."""

def print_iter(iterator):
    """
    Função auxiliar para imprimir todos os itens de um iterador.
    Converte o iterador em uma lista e imprime cada elemento em uma nova linha.
    """
    print(*list(iterator), sep='\n')
    print()

produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]
"""
Lista de dicionários, onde cada dicionário representa um produto com seu nome e preço.
"""

def aumentar_porcentagem(valor, porcentagem):
    """
    Função que aumenta o valor de um produto por uma determinada porcentagem.
    Recebe dois argumentos: `valor` e `porcentagem`.
    Retorna o valor ajustado pela porcentagem, arredondado para duas casas decimais.
    """
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)
"""
Cria uma nova função `aumentar_dez_porcento` usando `partial`.
Essa função já tem a porcentagem de 10% (1.1) fixada, 
permitindo que ela seja aplicada a qualquer valor que for passado.
"""
def muda_preco_de_produtos(produto):
    """
    Função que cria um novo dicionário de produto com o preço ajustado em 10%.
    Recebe um dicionário `produto` como argumento.
    Retorna um novo dicionário com os mesmos dados do produto, mas com o preço atualizado.
    """
    return {
        **produto,  # Desempacota os dados do dicionário original.
        'preco': aumentar_dez_porcento(
            produto['preco']
        )  # Aplica o aumento de 10% no preço.
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))
"""
Usa `map` para aplicar a função `muda_preco_de_produtos` a cada item da lista `produtos`.
`map` retorna um iterador, que é convertido em uma lista para que os resultados possam ser usados.
O resultado é uma lista de novos produtos com os preços atualizados.
"""
print_iter(produtos)
"""Imprime os produtos originais usando a função `print_iter`."""

print_iter(novos_produtos)
"""Imprime os novos produtos com os preços ajustados usando a função `print_iter`."""

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)
"""
Usa `map` com uma função lambda que multiplica cada número por 3.
A lista `[1, 2, 3, 4]` é mapeada para `[3, 6, 9, 12]`.
`map` retorna um iterador, então ele é convertido em uma lista para que os resultados possam ser impressos.
"""
