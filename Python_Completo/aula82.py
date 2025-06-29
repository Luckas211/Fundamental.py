def executa(funcao, *args):
    """Executa a função com argumentos variáveis."""
    return funcao(*args)

"""
A função 'executa' recebe uma função 'funcao' como argumento, juntamente com argumentos variáveis 'args'.
Ela executa a função 'funcao' com os argumentos 'args' e retorna o resultado.
"""

# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,  # Define uma função lambda que duplica um número.
    2  # Define o multiplicador como 2.
)
print(duplica(2))  # Chama a função 'duplica' com o argumento 2 e imprime o resultado.

"""
Aqui, é criada uma função que duplica um número.
A função 'executa' é chamada com uma função lambda que retorna outra função lambda que multiplica 'n' por 'm',
juntamente com o argumento '2'.
O resultado é armazenado na variável 'duplica'.
Em seguida, a função 'duplica' é chamada com o argumento '2', resultando em '4' (2 * 2).
"""

print(
    executa(
        lambda x, y: x + y,  # Define uma função lambda que soma dois números.
        2, 3  # Define os números a serem somados como 2 e 3.
    )
)

"""
Aqui, é criada uma função que soma dois números.
A função 'executa' é chamada com uma função lambda que retorna a soma de 'x' e 'y',
juntamente com os argumentos '2' e '3'.
O resultado da soma é impresso.
"""

print(
    executa(
        lambda *args: sum(args),  # Define uma função lambda que soma todos os argumentos.
        1, 2, 3, 4, 5, 6, 7  # Define os números a serem somados como 1, 2, 3, 4, 5, 6, 7.
    )
)

"""
Aqui, é criada uma função que soma uma lista de números.
A função 'executa' é chamada com uma função lambda que retorna a soma de todos os argumentos,
juntamente com os argumentos '1, 2, 3, 4, 5, 6, 7'.
O resultado da soma é impresso.
"""
tri = executa(
    lambda m: lambda n: n * m,  # Define uma função lambda que duplica um número.
    5 # Define o multiplicador como 2.
)

