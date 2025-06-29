'''letra = {}
for letter in "Missisipi":
    letra[letter] = letra.get(letter,0) + 1 

print(letra)'''



'''def copiaArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, "r")
    f2 = open(novoArquivo, "w")
    while 1:
        texto = f1.read(50)
        if texto == "":
            break
        f2.write(texto)
    f1.close()
    f2.close()
    return


f = open("teste.dat", "w")
f.write("linha um\nlinha dois\nlinha três\n")
f.close()
f = open("teste.dat", "r")
print (f.readline())
print (f.readlines())




def filtraArquivo(velhoArquivo, novoArquivo):
    f1 = open(velhoArquivo, "r")
    f2 = open(novoArquivo, "w")
    while 1:
        texto = f1.readline()
        if texto == "":
            break
        if texto[0] == '#':
            continue
        f2.write(texto)
    f1.close()
    f2.close()
    return

filtraArquivo()()'''

import pandas as pd

# Criando a série
data = [1, 2, 3, 4, 5,6]
minha_serie = pd.Series(data)

# Indexando o primeiro elemento da série
primeiro_elemento = minha_serie[0]
print(f"Primeiro elemento: {primeiro_elemento}")
# Output esperado: 1

# Selecionando valores maiores que 3
valores_maiores_que_tres = minha_serie[minha_serie > 3]
print(f"Valores maiores que 3: {valores_maiores_que_tres.tolist()}")
# Output esperado: [4, 5]

# Operações matemáticas - Adicionando 10 a cada elemento da série
serie_somada = minha_serie + 10
print(f"Série somada com 10: {serie_somada.tolist()}")
# Output esperado: [11, 12, 13, 14, 15]

#pega a média da lista
print(minha_serie.mean())