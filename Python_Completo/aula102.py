# Definindo a função 'concatenar' que recebe uma string inicial como argumento
def concatenar(string_inicial):
    # Criando uma variável 'valor_final' que armazena a stri ng inicial
    valor_final = string_inicial

    # Definindo uma função interna 'interna' que recebe uma string para concatenar
    def interna(valor_a_concatenar=''):
        # Usando 'nonlocal' para permitir que 'valor_final' seja modificada dentro da função interna
        nonlocal valor_final
        # Concatenando a string recebida à variável 'valor_final'
        valor_final += valor_a_concatenar
        # Retornando o valor atualizado de 'valor_final'
        return valor_final
    
    # Retornando a função interna 'interna'
    return interna

# Chamando a função 'concatenar' com a string 'a' e armazenando a função interna retornada em 'c'
c = concatenar('a')

# Chamando a função interna 'c' com 'b', 'c', e 'd', respectivamente, e imprimindo os resultados
# A cada chamada, a string passada é concatenada à string acumulada em 'valor_final'
print(c('b'))  # Saída: 'ab'
print(c('c'))  # Saída: 'abc'
print(c('d'))  # Saída: 'abcd'

# Chamando a função 'c' sem nenhum argumento, apenas para obter o valor final acumulado
final = c()
# Imprimindo o valor final acumulado
print(final)  # Saída: 'abcd'



'''def funcao_externa():
    x = 10
    def funcao_interna():
        nonlocal x
        x +=1

    funcao_interna()
    print(x)
        

funcao_externa()

x1 = 20

def modificar_global():
    global x1
    x1 += 1

modificar_global()
print(x1)


def varivel_livre_externa():
    x2 = 30

    def varivel_livre_interna():
        print(x2)

    varivel_livre_interna()
varivel_livre_externa()
'''
