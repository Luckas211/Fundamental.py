# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis

# Tipos Mutáveis: listas, dicionários, conjuntos
# Tipos Imutáveis: tuplas, strings, números, None, False, range

# Definindo variáveis de vários tipos
lista = []  # Lista vazia (Mutável)
"""Uma lista vazia é um tipo mutável e é considerada Falsy."""

dicionario = {}  # Dicionário vazio (Mutável)
"""Um dicionário vazio é um tipo mutável e é considerado Falsy."""

conjunto = set()  # Conjunto vazio (Mutável)
"""Um conjunto vazio é um tipo mutável e é considerado Falsy."""

tupla = ()  # Tupla vazia (Imutável)
"""Uma tupla vazia é um tipo imutável e é considerada Falsy."""

string = ''  # String vazia (Imutável)
"""Uma string vazia é um tipo imutável e é considerada Falsy."""

inteiro = 0  # Inteiro (Imutável)
"""O valor inteiro 0 é um tipo imutável e é considerado Falsy."""

flutuante = 0.0  # Float (Imutável)
"""O valor float 0.0 é um tipo imutável e é considerado Falsy."""

nada = None  # NoneType (Imutável)
"""O valor None é um tipo imutável e é considerado Falsy."""

falso = False  # Boolean (Imutável)
"""O valor False é um tipo imutável e é considerado Falsy."""

intervalo = range(0)  # Range vazio (Imutável)
"""Um objeto range vazio é um tipo imutável e é considerado Falsy."""

# Função para verificar se o valor é Truthy ou Falsy
def falsy(valor):
    return 'falsy' if not valor else 'truthy'
"""A função falsy() retorna 'falsy' se o valor for considerado falso e 'truthy' caso contrário."""

# Testando valores e imprimindo se são Truthy ou Falsy
print(f'TESTE: {falsy("TESTE")}')
"""Imprime 'truthy' porque a string 'TESTE' não está vazia."""

print(f'{lista=}, {falsy(lista)}')
"""Imprime 'lista=[], falsy' porque uma lista vazia é Falsy."""

print(f'{dicionario=}, {falsy(dicionario)}')
"""Imprime 'dicionario={}, falsy' porque um dicionário vazio é Falsy."""

print(f'{conjunto=}, {falsy(conjunto)}')
"""Imprime 'conjunto=set(), falsy' porque um conjunto vazio é Falsy."""

print(f'{tupla=}, {falsy(tupla)}')
"""Imprime 'tupla=(), falsy' porque uma tupla vazia é Falsy."""

print(f'{string=}, {falsy(string)}')
"""Imprime 'string='', falsy' porque uma string vazia é Falsy."""

print(f'{inteiro=}, {falsy(inteiro)}')
"""Imprime 'inteiro=0, falsy' porque o inteiro 0 é Falsy."""

print(f'{flutuante=}, {falsy(flutuante)}')
"""Imprime 'flutuante=0.0, falsy' porque o float 0.0 é Falsy."""

print(f'{nada=}, {falsy(nada)}')
"""Imprime 'nada=None, falsy' porque o valor None é Falsy."""

print(f'{falso=}, {falsy(falso)}')
"""Imprime 'falso=False, falsy' porque o valor False é Falsy."""

print(f'{intervalo=}, {falsy(intervalo)}')
"""Imprime 'intervalo=range(0, 0), falsy' porque um range vazio é Falsy."""
