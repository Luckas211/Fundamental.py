# Importa o módulo 'os' para o comando 'clear' (limpar o terminal)
import os

# Função para listar as tarefas
def listar(tarefas):
    """
    Exibe as tarefas da lista atual. Se a lista estiver vazia, mostra uma mensagem informando.
    """
    print()  # Linha em branco para separar visualmente
    if not tarefas:  # Verifica se a lista de tarefas está vazia
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:  # Itera sobre a lista de tarefas
        print(f'\t{tarefa}')  # Imprime cada tarefa com tabulação
    print()  # Linha em branco no final

# Função para desfazer a última tarefa
def desfazer(tarefas, tarefas_refazer):
    """
    Remove a última tarefa da lista principal e a coloca na lista de tarefas desfeitas (para refazer depois).
    """
    print()  # Linha em branco
    if not tarefas:  # Verifica se há tarefas para desfazer
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()  # Remove a última tarefa
    print(f'{tarefa=} removida da lista de tarefas.')  # Exibe qual tarefa foi removida
    tarefas_refazer.append(tarefa)  # Adiciona a tarefa removida à lista de refazer
    print()  # Linha em branco
    listar(tarefas)  # Mostra a lista atualizada de tarefas

# Função para refazer uma tarefa desfeita
def refazer(tarefas, tarefas_refazer):
    """
    Recupera a última tarefa desfeita e a adiciona de volta à lista principal de tarefas.
    """
    print()  # Linha em branco
    if not tarefas_refazer:  # Verifica se há tarefas para refazer
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()  # Remove a última tarefa da lista de refazer
    print(f'{tarefa=} adicionada na lista de tarefas.')  # Exibe qual tarefa foi refeita
    tarefas.append(tarefa)  # Adiciona de volta à lista de tarefas
    print()  # Linha em branco
    listar(tarefas)  # Exibe a lista atualizada de tarefas

# Função para adicionar uma nova tarefa
def adicionar(tarefa, tarefas):
    """
    Adiciona uma nova tarefa à lista de tarefas, se o usuário tiver digitado algo.
    """
    print()  # Linha em branco
    tarefa = tarefa.strip()  # Remove espaços extras no início e no final
    if not tarefa:  # Verifica se o usuário não digitou nada
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')  # Exibe a tarefa que foi adicionada
    tarefas.append(tarefa)  # Adiciona a tarefa à lista
    print()  # Linha em branco
    listar(tarefas)  # Exibe a lista atualizada de tarefas

# Inicializa as listas de tarefas e tarefas desfeitas
tarefas = []  # Lista para as tarefas atuais
tarefas_refazer = []  # Lista para as tarefas desfeitas (que podem ser refeitas)

# Loop principal do programa
while True:
    # Exibe as opções de comandos
    print('Comandos: listar, desfazer, refazer e clear')
    
    # Captura a entrada do usuário (uma tarefa ou comando)
    tarefa = input('Digite uma tarefa ou comando: ')

    # Dicionário de comandos, associando cada comando a uma função correspondente
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),  # Limpa o terminal
        'adicionar': lambda: adicionar(tarefa, tarefas),  # Adiciona uma tarefa à lista
    }

    # Verifica se a entrada do usuário é um comando válido
    comando = comandos.get(tarefa)  # Busca o comando no dicionário

    if comando:  # Se for um comando, executa a função correspondente
        comando()
    else:  # Caso contrário, assume que é uma tarefa e a adiciona à lista
        adicionar(tarefa, tarefas)


'''Explicação detalhada:
Importação de os:

Usamos os.system('clear') para limpar o terminal sempre que o comando "clear" for digitado.
Função listar(tarefas):

Lista todas as tarefas na lista atual. Se a lista estiver vazia, uma mensagem será exibida informando que não há tarefas.
Função desfazer(tarefas, tarefas_refazer):

Remove a última tarefa da lista e a adiciona à lista de tarefas desfeitas, permitindo que ela seja refeita posteriormente.
Função refazer(tarefas, tarefas_refazer):

Recupera a última tarefa desfeita da lista de refazer e a coloca de volta na lista principal de tarefas.
Função adicionar(tarefa, tarefas):

Adiciona uma nova tarefa à lista, removendo quaisquer espaços extras digitados pelo usuário.
Dicionário de comandos:

Um dicionário (comandos) foi criado para associar as entradas do usuário com as funções correspondentes. Isso simplifica o código ao substituir os muitos if e elif por um mapeamento direto.
Se o usuário digitar um comando, ele será buscado no dicionário, e a função associada será executada. Caso a entrada não seja um comando válido, o programa a trata como uma tarefa e a adiciona à lista.
Exemplo de uso:
O usuário pode adicionar tarefas digitando-as diretamente.
Pode usar "listar" para exibir todas as tarefas, "desfazer" para remover a última tarefa e "refazer" para restaurar a tarefa desfeita.
"clear" limpa o terminal, melhorando a visualização.'''