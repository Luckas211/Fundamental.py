# Funções recursivas e recursividade
# - Funções recursivas são funções que podem se chamar de volta (ou seja, elas chamam a si mesmas).
# - São úteis para dividir problemas grandes em partes menores e mais gerenciáveis.
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores.
# - Um caso recursivo que resolve o pequeno problema.
# - Um caso base que para a recursão, evitando um loop infinito.

# Exemplo clássico de recursividade: cálculo do fatorial.
# O fatorial de n (n!) é o produto de todos os números inteiros positivos até n.
# Por exemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120.
# (Mais sobre fatorial em: https://brasilescola.uol.com.br/matematica/fatorial.htm)

# Função recursiva que imprime uma sequência de números até um valor final
def recursiva(inicio=0, fim=4):  # Define a função 'recursiva' com dois parâmetros: 'inicio' e 'fim', ambos com valores padrão.
    print(inicio, fim)  # Imprime os valores atuais de 'inicio' e 'fim' em cada chamada da função.

    # Caso base: se o 'inicio' for maior ou igual ao 'fim', a função retorna o valor de 'fim' e a recursão para.
    if inicio >= fim:
        return fim

    # Caso recursivo: aumenta o valor de 'inicio' em 1 e chama a função recursivamente.
    inicio += 1
    return recursiva(inicio, fim)  # A função chama a si mesma com o novo valor de 'inicio'.

# Chama a função recursiva e imprime o resultado final.
print(recursiva())  # A chamada inicial usa os valores padrão: inicio=0 e fim=4.
print("----Abaixo é meu código----")

def recursiva2(ini=0, final=9):
    print(ini,final)
    if ini >= final:
        return final
    ini += 1
    return recursiva2(ini,final)
    

recursiva2()