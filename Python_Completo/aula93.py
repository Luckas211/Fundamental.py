# (Parte 1) try e except para tratar exceções

# Exemplo de código que causa uma exceção
# a = 18  # Define a variável 'a' como 18
# b = 0  # Define a variável 'b' como 0, o que causará um erro ao tentar dividir por ela
# c = a / b  # Tenta dividir 'a' por 'b', o que causará um ZeroDivisionError

try:
    a = 18  # Define a variável 'a' como 18
    b = 0  # Define a variável 'b' como 0
    # print(b[0])  # Exemplo de código que causaria um TypeError se descomentado (inteiro não é indexável)
    print('Linha 1'[1000])  # Tenta acessar um índice fora do intervalo, causando um IndexError
    c = a / b  # Tenta dividir 'a' por 'b', o que causará um ZeroDivisionError
    print('Linha 2')  # Esta linha não será executada se ocorrer uma exceção acima
except ZeroDivisionError:  # Trata especificamente a exceção de divisão por zero
    print('Dividiu por zero.')
    """Captura e trata o ZeroDivisionError, imprimindo uma mensagem específica"""
except NameError:  # Trata especificamente a exceção de nome não definido
    print('Nome b não está definido')
    """Captura e trata o NameError, imprimindo uma mensagem específica"""
except (TypeError, IndexError):  # Trata múltiplas exceções (TypeError e IndexError)
    print('TypeError + IndexError')
    """Captura e trata os erros TypeError e IndexError, imprimindo uma mensagem específica"""
except Exception:  # Captura qualquer outra exceção não tratada acima
    print('ERRO DESCONHECIDO.')
    """Captura e trata qualquer exceção que não foi específica acima, imprimindo uma mensagem de erro desconhecido"""

print('CONTINUAR')  # Esta linha será executada mesmo se houver uma exceção
"""Imprime 'CONTINUAR' para indicar que o programa continuou executando após o bloco try/except"""

# Saída esperada:
# TypeError + IndexError
# CONTINUAR


# (Parte 2) try e except para tratar exceções

# Exemplo de código que causa uma exceção
# a = 18  # Define a variável 'a' como 18
# b = 0  # Define a variável 'b' como 0, o que causará um erro ao tentar dividir por ela
# c = a / b  # Tenta dividir 'a' por 'b', o que causará um ZeroDivisionError

try:
    a = 18  # Define a variável 'a' como 18
    b = 0  # Define a variável 'b' como 0
    # print(b[0])  # Exemplo de código que causaria um TypeError se descomentado (inteiro não é indexável)
    # print('Linha 1'[1000])  # Exemplo de código que causaria um IndexError se descomentado (índice fora do intervalo)
    c = a / b  # Tenta dividir 'a' por 'b', o que causará um ZeroDivisionError
    print('Linha 2')  # Esta linha não será executada se ocorrer uma exceção acima
except ZeroDivisionError as e:  # Trata especificamente a exceção de divisão por zero
    print(e.__class__.__name__)  # Imprime o nome da classe da exceção
    """Imprime o nome da exceção ZeroDivisionError"""
    print(e)  # Imprime a mensagem de erro da exceção
    """Imprime a mensagem de erro associada ao ZeroDivisionError"""
except NameError:  # Trata especificamente a exceção de nome não definido
    print('Nome b não está definido')
    """Captura e trata o NameError, imprimindo uma mensagem específica"""
except (TypeError, IndexError) as error:  # Trata múltiplas exceções (TypeError e IndexError)
    print('TypeError + IndexError')  # Indica que ocorreu um TypeError ou IndexError
    """Indica que ocorreu um erro do tipo TypeError ou IndexError"""
    print('MSG:', error)  # Imprime a mensagem de erro da exceção
    """Imprime a mensagem de erro associada ao TypeError ou IndexError"""
    print('Nome:', error.__class__.__name__)  # Imprime o nome da classe da exceção
    """Imprime o nome da exceção que ocorreu (TypeError ou IndexError)"""
except Exception:  # Captura qualquer outra exceção não tratada acima
    print('ERRO DESCONHECIDO.')
    """Captura e trata qualquer exceção que não foi específica acima, imprimindo uma mensagem de erro desconhecido"""

print('CONTINUAR')  # Esta linha será executada mesmo se houver uma exceção
"""Imprime 'CONTINUAR' para indicar que o programa continuou executando após o bloco try/except"""

# Saída esperada:
# ZeroDivisionError
# division by zero
# CONTINUAR


try:
    print("Inicio")
    nome = ("Lucas", ué)
    print(nome)

except NameError as cade:
    print(cade.__class__.__name__)

finally:
    print("ok")