# Lista de perguntas, cada uma com suas opções e a resposta correta.
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',  # Primeira pergunta.
        'Opções': ['1', '3', '4', '5'],  # Opções de resposta para a primeira pergunta.
        'Resposta': '4',  # Resposta correta para a primeira pergunta.
    },
    {
        'Pergunta': 'Quanto é 5*5?',  # Segunda pergunta.
        'Opções': ['25', '55', '10', '51'],  # Opções de resposta para a segunda pergunta.
        'Resposta': '25',  # Resposta correta para a segunda pergunta.
    },
    {
        'Pergunta': 'Quanto é 10/2?',  # Terceira pergunta.
        'Opções': ['4', '5', '2', '1'],  # Opções de resposta para a terceira pergunta.
        'Resposta': '5',  # Resposta correta para a terceira pergunta.
    },
]

"""
A lista 'perguntas' contém três dicionários, cada um representando uma pergunta. 
Cada dicionário inclui a chave 'Pergunta' para a pergunta, 'Opções' para as opções de resposta, 
e 'Resposta' para a resposta correta.
"""

qtd_acertos = 0  # Variável para contar o número de acertos do usuário.
"""
'qtd_acertos' é uma variável que conta o número de respostas corretas do usuário.
"""

for pergunta in perguntas:  # Loop que percorre cada pergunta na lista de perguntas.
    """
    O loop 'for' itera sobre cada dicionário na lista 'perguntas'. 
    Cada dicionário é armazenado na variável 'pergunta' durante cada iteração.
    """
    
    print('Pergunta:', pergunta['Pergunta'])  # Exibe a pergunta atual.
    print()  # Imprime uma linha em branco para separar a pergunta das opções.

    opcoes = pergunta['Opções']  # Obtém a lista de opções de resposta da pergunta atual.
    
    for i, opcao in enumerate(opcoes):  # Itera sobre as opções com seus índices.
        print(f'{i})', opcao)  # Exibe cada opção numerada.
    print()  # Imprime uma linha em branco para separar as opções da entrada do usuário.

    """
    A pergunta e as opções são exibidas no console. 
    'enumerate(opcoes)' permite iterar sobre a lista de opções, fornecendo tanto o índice quanto o valor de cada opção.
    """
    
    escolha = input('Escolha uma opção: ')  # Solicita a escolha do usuário.
    
    """
    'input()' exibe a mensagem 'Escolha uma opção:' e lê a entrada do usuário, armazenando-a na variável 'escolha'.
    """
    
    acertou = False  # Variável para verificar se o usuário acertou a resposta.
    escolha_int = None  # Variável para armazenar a escolha convertida para inteiro.
    qtd_opcoes = len(opcoes)  # Número total de opções disponíveis.

    if escolha.isdigit():  # Verifica se a escolha do usuário é um número.
        escolha_int = int(escolha)  # Converte a escolha para inteiro.

    if escolha_int is not None:  # Verifica se a escolha convertida é um índice válido de opção.
        if escolha_int >= 0 and escolha_int < qtd_opcoes:  # Verifica se a escolha está dentro do intervalo de opções.
            if opcoes[escolha_int] == pergunta['Resposta']:  # Compara a opção escolhida com a resposta correta.
                acertou = True  # Marca como acerto se a resposta estiver correta.

    """
    Este bloco verifica se a escolha do usuário é válida:
    - Verifica se 'escolha' é um número.
    - Converte 'escolha' para um inteiro.
    - Verifica se 'escolha_int' é um índice válido na lista de opções.
    - Compara a opção escolhida com a resposta correta.
    """
    
    print()  # Imprime uma linha em branco para separar a resposta do próximo bloco.
    
    if acertou:  # Exibe o resultado da resposta do usuário.
        qtd_acertos += 1  # Incrementa a contagem de acertos.
        print('Acertou 👍')  # Informa que o usuário acertou.
    else:
        print('Errou ❌')  # Informa que o usuário errou.
    
    print()  # Imprime uma linha em branco para separar a próxima pergunta.
    
    """
    Exibe se o usuário acertou ou errou e atualiza a contagem de acertos.
    """

print('Você acertou', qtd_acertos)  # Exibe o número total de acertos.
print('de', len(perguntas), 'perguntas.')  # Exibe o número total de perguntas respondidas.

"""
No final, exibe o total de perguntas que o usuário acertou e o número total de perguntas respondidas.
"""
