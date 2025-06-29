# raise - lançando exceções (erros)
# Link para a documentação oficial: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    """Função que verifica se o divisor é zero e lança uma exceção se for"""
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    """Levanta uma exceção ZeroDivisionError se d for zero"""
    return True

def deve_ser_int_ou_float(n):
    """Função que verifica se o valor é do tipo int ou float e lança uma exceção se não for"""
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    """Levanta uma exceção TypeError se n não for int ou float"""
    return True

def divide(n, d):
    """Função que realiza a divisão, após verificar os tipos dos valores e se o divisor é zero"""
    deve_ser_int_ou_float(n)
    """Verifica se n é int ou float"""
    deve_ser_int_ou_float(d)
    """Verifica se d é int ou float"""
    nao_aceito_zero(d)
    """Verifica se d é zero"""
    return n / d

# Testa a função divide com valores inválidos
print(divide(8, '0'))
"""Tenta dividir 8 por uma string '0', o que causará uma exceção TypeError"""
