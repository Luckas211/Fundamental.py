# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func):
    """
    Define uma função decoradora chamada `criar_funcao` que aceita uma função `func` 
    como argumento. Esta função irá retornar uma nova função que adiciona 
    funcionalidades à função original.
    """
    def interna(*args, **kwargs):
        """
        Define a função interna (wrapper) que será retornada. 
        Ela aceita qualquer número de argumentos posicionais e nomeados 
        e adiciona funcionalidades antes e depois da execução da função original.
        """
        print('Vou te decorar')
        # Imprime uma mensagem indicando que a função está sendo "decorada".

        for arg in args:
            e_string(arg)
            """
            Itera sobre cada argumento em `args` e chama a função `e_string` 
            para verificar se cada argumento é uma string. Se algum argumento 
            não for uma string, uma exceção `TypeError` será levantada.
            """

        resultado = func(*args, **kwargs)
        """ 
        Chama a função original (`func`) com os argumentos recebidos 
        e armazena o resultado em `resultado`.
        """

        print(f'O seu resultado foi {resultado}.')
        # Imprime o resultado da função original.

        print('Ok, agora você foi decorada')
        # Imprime uma mensagem indicando que a função foi decorada.

        return resultado
        """ 
        Retorna o resultado da função original, garantindo que a função 
        decorada se comporte como a original, mas com funcionalidades adicionais.
        """
    return interna
    """ 
    Retorna a função `interna`, que substituirá a função original 
    ao aplicar o decorador.
    """

def inverte_string(string):
    """ 
    Define uma função simples que recebe uma string e retorna a string invertida.
    """
    return string[::-1]
    # Retorna a string invertida usando slicing.

def e_string(param):
    """ 
    Define uma função que verifica se o parâmetro fornecido é uma string.
    Se o parâmetro não for uma string, levanta uma exceção `TypeError`.
    """
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
        # Levanta um erro se `param` não for uma string.

inverte_string_checando_parametro = criar_funcao(inverte_string)
"""
Aplica a função decoradora `criar_funcao` à função `inverte_string`.
Isso retorna uma nova função `inverte_string_checando_parametro` que 
inclui as verificações e mensagens adicionais definidas em `interna`.
"""

invertida = inverte_string_checando_parametro('123')
"""
Chama a função decorada `inverte_string_checando_parametro` com o argumento '123'.
Isso executa as verificações de tipo, inverte a string, imprime as mensagens adicionais, 
e retorna a string invertida.
"""

print(invertida)
# Imprime a string invertida, que deve ser '321'.
 