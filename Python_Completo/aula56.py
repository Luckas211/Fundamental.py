# Dividindo a string 'frase' em uma lista de substrings usando ',' como delimitador
lista_frases_cruas = frase.split(',')

# Criando uma lista vazia para armazenar as frases processadas
lista_frases = []

# Iterando sobre cada elemento (frase) na lista 'lista_frases_cruas'
for i, frase in enumerate(lista_frases_cruas):
    # Removendo espaços em branco adicionais no início e no fim da frase e adicionando à lista 'lista_frases'
    lista_frases.append(lista_frases_cruas[i].strip())

# Unindo as frases da lista 'lista_frases' em uma única string, separadas por ', '
frases_unidas = ', '.join(lista_frases)

# Imprimindo a string resultante após a união das frases
print(frases_unidas)

"""
split - divide uma string em uma lista de substrings com base em um delimitador especificado.
join - une uma lista de substrings em uma única string, utilizando um separador especificado entre cada elemento.
"""
