# Função recursiva simples e cálculo de fatorial

# Função recursiva que imprime uma sequência de números até um valor final
def recursiva(inicio=0, fim=4):
    # A função imprime os valores atuais de 'inicio' e 'fim' em cada chamada
    print(inicio, fim)

    # Caso base: se 'inicio' for maior ou igual a 'fim', a função para e retorna 'fim'
    if inicio >= fim:
        return fim

    # Caso recursivo: incrementa 'inicio' e chama a função novamente com o novo valor
    inicio += 1
    return recursiva(inicio, fim)

# Chama a função recursiva com os valores padrão e imprime o resultado
print(recursiva())


# Função para calcular o fatorial de um número usando recursão
def factorial(n):
    # Caso base: se 'n' for menor ou igual a 1, retorna 1
    if n <= 1:
        return 1

    # Caso recursivo: multiplica 'n' pelo fatorial de 'n-1'
    return n * factorial(n - 1)

# Calcula e imprime o fatorial de 5, 10 e 100
print(factorial(5))   # 5! = 120
print(factorial(10))  # 10! = 3.628.800
print(factorial(100)) # 100! é um número muito grande
