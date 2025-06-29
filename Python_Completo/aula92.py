# Yield from em Python

def gen1():
    print('COMECOU GEN1')  # Indica o início da execução de gen1
    yield 1  # Produz o valor 1
    yield 2  # Produz o valor 2
    yield 3  # Produz o valor 3
    print('ACABOU GEN1')  # Indica o fim da execução de gen1
"""Função geradora 'gen1' que produz os valores 1, 2, 3 e imprime mensagens no início e no fim"""

def gen3():
    print('COMECOU GEN3')  # Indica o início da execução de gen3
    yield 10  # Produz o valor 10
    yield 20  # Produz o valor 20
    yield 30  # Produz o valor 30
    print('ACABOU GEN3')  # Indica o fim da execução de gen3
"""Função geradora 'gen3' que produz os valores 10, 20, 30 e imprime mensagens no início e no fim"""

def gen2(gen=None):
    print('COMECOU GEN2')  # Indica o início da execução de gen2
    if gen is not None:  # Verifica se um gerador foi passado como argumento
        yield from gen  # Delegação para o gerador passado como argumento
        """Se um gerador 'gen' for fornecido, delega a iteração para esse gerador usando 'yield from'"""
    yield 4  # Produz o valor 4
    yield 5  # Produz o valor 5
    yield 6  # Produz o valor 6
    print('ACABOU GEN2')  # Indica o fim da execução de gen2
"""Função geradora 'gen2' que produz os valores 4, 5, 6 e, opcionalmente, delega a iteração para outro gerador"""

# Criando instâncias das funções geradoras
g1 = gen2(gen1())  # Cria um gerador 'g1' que delega a iteração para 'gen1'
"""Cria o gerador 'g1' que chama 'gen2' com 'gen1' como argumento, portanto, itera através de 'gen1' primeiro"""
g2 = gen2(gen3())  # Cria um gerador 'g2' que delega a iteração para 'gen3'
"""Cria o gerador 'g2' que chama 'gen2' com 'gen3' como argumento, portanto, itera através de 'gen3' primeiro"""
g3 = gen2()  # Cria um gerador 'g3' que não delega a iteração para nenhum gerador
"""Cria o gerador 'g3' que chama 'gen2' sem argumentos, portanto, não itera através de nenhum outro gerador"""

# Iterando sobre o gerador 'g1'
for numero in g1:
    print(numero)  # Imprime cada número produzido por 'g1'
"""Itera através do gerador 'g1', que primeiro itera através de 'gen1' e depois produz 4, 5, 6"""
print()

# Iterando sobre o gerador 'g2'
for numero in g2:
    print(numero)  # Imprime cada número produzido por 'g2'
"""Itera através do gerador 'g2', que primeiro itera através de 'gen3' e depois produz 4, 5, 6"""
print()

# Iterando sobre o gerador 'g3'
for numero in g3:
    print(numero)  # Imprime cada número produzido por 'g3'
"""Itera através do gerador 'g3', que produz 4, 5, 6 sem delegar a iteração para nenhum outro gerador"""
print()

# Saída esperada:
# COMECOU GEN2
# COMECOU GEN1
# 1
# 2
# 3
# ACABOU GEN1
# 4
# 5
# 6
# ACABOU GEN2

# COMECOU GEN2
# COMECOU GEN3
# 10
# 20
# 30
# ACABOU GEN3
# 4
# 5
# 6
# ACABOU GEN2

# COMECOU GEN2
# 4
# 5
# 6
# ACABOU GEN2
