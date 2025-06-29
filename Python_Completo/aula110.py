'''
from itertools import groupby

palavras = ["Laranja","Tangerina","Kiwi","Banana"]
grupos = groupby(palavras, key=lambda x: len(x))
juntos = groupby(palavras)

for indices, grupo in juntos:
    print(indices, *list(grupo))

'''

# Importando a função groupby do módulo itertools.
# - groupby: Agrupa elementos de um iterável que possuem a mesma chave, quando ordenados previamente.
from itertools import groupby

# Lista de dicionários onde cada dicionário representa um aluno com seu nome e nota.
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# Função que retorna a nota do aluno. Será usada para ordenação e agrupamento.
def ordena(aluno):
    return aluno['nota']

# Ordena a lista de alunos pela nota usando a função 'ordena' como chave de ordenação.
alunos_agrupados = sorted(alunos, key=ordena)

# Agrupa os alunos com base na nota, utilizando a função 'ordena' como chave.
grupos = groupby(alunos_agrupados, key=ordena)

# Itera pelos grupos formados pelo groupby.
for chave, grupo in grupos:
    # Imprime a chave do grupo (neste caso, a nota).
    print(chave)
    # Itera sobre os alunos dentro de cada grupo e imprime suas informações.
    for aluno in grupo:
        print(aluno)