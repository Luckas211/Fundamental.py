produtos = [{"nome":"produto 2","preco": 10.00},
            {"nome":"produto 3","preco": 45.00},
            {"nome":"produto 1","preco": 36.10},
            {"nome":"produto 4","preco": 220.00}]


'''for p in produtos:
    if p["preco"] > 40:
        print(p)'''

filtro_de_indice = filter(lambda p: p["nome"] > "produto 0", produtos)
filtro_de_preco = filter(lambda p: p["preco"] > 40, produtos)

print(*list(filtro_de_indice),sep="\n")
print()
print(*list(filtro_de_preco),sep="\n")

