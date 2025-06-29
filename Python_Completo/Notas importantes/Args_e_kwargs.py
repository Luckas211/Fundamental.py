def soma(*args):
    """ 
    Define a função `soma`, que aceita um número variável de argumentos posicionais 
    e retorna a soma desses valores.
    """
    return sum(args)
    """ 
    Usa a função `sum` para calcular a soma de todos os valores passados em `args` 
    e retorna o resultado.
    """

print(soma(1, 5, 7))
""" 
Chama a função `soma` com os argumentos 1, 5 e 7. 
A soma desses valores (13) será impressa.
"""

print(soma(4, 5, 5, 5, 4))
""" 
Chama a função `soma` com os argumentos 4, 5, 5, 5 e 4. 
A soma desses valores (23) será impressa.
"""

def exibir_info(**kwargs):
    """ 
    Define a função `exibir_info`, que aceita um número variável de argumentos nomeados 
    (kwargs) e os imprime no formato "chave: valor".
    """
    for chave, valor in kwargs.items():
        """
        Itera sobre os pares chave-valor no dicionário `kwargs`.
        Para cada par, a chave e o valor são extraídos.
        """
        print(f"{chave}: {valor}")
        """ 
        Imprime cada par `chave: valor` no formato "chave: valor".
        """

exibir_info(nome="Lucas", idade=25, cidade="Rio de Janeiro")
""" 
Chama a função `exibir_info` com três argumentos nomeados:
- `nome` com o valor "Lucas"
- `idade` com o valor 25
- `cidade` com o valor "Rio de Janeiro"

A função irá imprimir:
nome: Lucas
idade: 25
cidade: Rio de Janeiro
"""
