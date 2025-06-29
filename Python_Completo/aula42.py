frase = 'aaaaooo'  # Definindo a string que queremos analisar

i = 0  # Inicializando um contador para percorrer a string
qtd_apareceu_mais_vezes = 0  # Inicializando a quantidade de vezes que a letra mais comum apareceu
letra_apareceu_mais_vezes = ''  # Inicializando a letra que apareceu mais vezes

while i < len(frase):  # Enquanto não tivermos percorrido toda a string
    letra_atual = frase[i]  # Pegando a letra atual

    if letra_atual == ' ':  # Se a letra for um espaço em branco
        i += 1  # Apenas passamos para a próxima letra
        continue

    qtd_atual = frase.count(letra_atual)  # Contando quantas vezes a letra atual aparece na string

    if qtd_apareceu_mais_vezes <= qtd_atual:  # Se a quantidade atual de aparições for maior ou igual à quantidade de aparições da letra mais comum até agora
        qtd_apareceu_mais_vezes = qtd_atual  # Atualizamos a quantidade de aparições mais comum
        letra_apareceu_mais_vezes = letra_atual  # Atualizamos a letra mais comum

    i += 1  # Passamos para a próxima letra

# Imprimindo o resultado
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
