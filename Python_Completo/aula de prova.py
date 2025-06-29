'''def funcao_externa():
    x = 10
    def funcao_interna():
        nonlocal x
        x +=1

    funcao_interna()
    print(x)
        

funcao_externa()

x1 = 20

def modificar_global():
    global x1
    x1 += 1

modificar_global()
print(x1)


def varivel_livre_externa():
    x2 = 30

    def varivel_livre_interna():
        print(x2)

    varivel_livre_interna()
varivel_livre_externa()
'''
