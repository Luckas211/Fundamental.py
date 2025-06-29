# Importa o módulo 'os' para permitir o uso do comando 'clear' (limpar o terminal)
import os

# Função para listar as tarefas atuais
def listar(tarefas):
    """
    Exibe a lista de tarefas. Se não houver tarefas, exibe uma mensagem informando isso.
    """
    print()  # Apenas para criar uma linha em branco no terminal
    if not tarefas:  # Verifica se a lista de tarefas está vazia
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:  # Itera sobre a lista de tarefas e imprime cada uma
        print(f'\t{tarefa}')  # '\t' é usado para adicionar uma tabulação antes da tarefa
    print()  # Outra linha em branco para separar visualmente

# Função para desfazer a última tarefa
def desfazer(tarefas, tarefas_refazer):
    """
    Remove a última tarefa da lista de tarefas e a move para a lista de tarefas para refazer.
    """
    print()  # Linha em branco
    if not tarefas:  # Verifica se há tarefas para desfazer
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()  # Remove e captura a última tarefa da lista
    print(f'{tarefa=} removida da lista de tarefas.')  # Exibe a tarefa que foi removida
    tarefas_refazer.append(tarefa)  # Adiciona a tarefa removida à lista de tarefas para refazer
    print()  # Linha em branco

# Função para refazer uma tarefa desfeita
def refazer(tarefas, tarefas_refazer):
    """
    Move a última tarefa da lista de refazer de volta para a lista de tarefas.
    """
    print()  # Linha em branco
    if not tarefas_refazer:  # Verifica se há tarefas para refazer
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()  # Remove a última tarefa da lista de refazer
    print(f'{tarefa=} adicionada na lista de tarefas.')  # Exibe a tarefa que foi refeita
    tarefas.append(tarefa)  # Adiciona a tarefa de volta à lista principal de tarefas
    print()  # Linha em branco

# Função para adicionar uma nova tarefa
def adicionar(tarefa, tarefas):
    """
    Adiciona uma nova tarefa à lista de tarefas, caso ela não seja vazia.
    """
    print()  # Linha em branco
    tarefa = tarefa.strip()  # Remove espaços em branco no início e no final da tarefa
    if not tarefa:  # Verifica se a tarefa é uma string vazia
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')  # Exibe a tarefa que foi adicionada
    tarefas.append(tarefa)  # Adiciona a tarefa à lista de tarefas
    print()  # Linha em branco

# Listas que armazenam as tarefas e as tarefas que foram desfeitas
tarefas = []  # Lista de tarefas principais
tarefas_refazer = []  # Lista de tarefas que foram desfeitas e podem ser refeitas

# Loop principal do programa
while True:
    # Exibe as opções de comandos disponíveis
    print('Comandos: listar, desfazer, refazer, clear')
    
    # Captura a entrada do usuário
    tarefa = input('Digite uma tarefa ou comando: ')

    # Verifica qual comando foi digitado e executa a função correspondente
    if tarefa == 'listar':
        listar(tarefas)  # Chama a função para listar as tarefas
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)  # Chama a função para desfazer a última tarefa
        listar(tarefas)  # Lista as tarefas após desfazer
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)  # Chama a função para refazer uma tarefa desfeita
        listar(tarefas)  # Lista as tarefas após refazer
        continue
    elif tarefa == 'clear':
        os.system('cls')  # Limpa o terminal (funciona no Linux/Mac; use 'cls' no Windows)
        continue
    else:
        adicionar(tarefa, tarefas)  # Adiciona uma nova tarefa à lista
        listar(tarefas)  # Lista as tarefas após adicionar a nova
        continue
