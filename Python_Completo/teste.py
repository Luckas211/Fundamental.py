from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator),sep="\n")
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem = 1.1)

print(aumentar_dez_porcento(22))

novos_produtos = [{**p, "preco": aumentar_dez_porcento(p["preco"])} for p in produtos]
verificar_apenas_preco = [produtos["preco"] for produtos in novos_produtos]
verificar_apenas_nome = [produtos["nome"]for produtos in novos_produtos]


print(verificar_apenas_preco)
print(verificar_apenas_nome)
print("-----Divisão-----")


def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))


print_iter(produtos)
print("--------------")
print_iter(novos_produtos)

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)
