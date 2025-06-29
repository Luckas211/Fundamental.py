'''
def validar():
    def validar_interna():
        print("Essa é a função interna")
    
    def outra_funcao():
        print("Essa é a outra função interna")
    
    def terceira_funcao():
        print("Essa é a terceira função interna")
    
    # Retorna um dicionário com as referências para as funções internas
    return {"validar_interna":validar_interna,"outra_funcao":outra_funcao}

# Obtendo o dicionário com as funções internas
funcoes = validar()

funcoes["validar_interna"]()
funcoes["outra_funcao"]()
'''

def sequencias():
    def sequencias_1():
        print("Primeira")
        def sequencias_2():
            print("Segunda")
        def sequencias_3(x,y):
            print("terceira")
            resultado = x+y
            print(resultado)

            
        sequencias_3(4,3)
    sequencias_1()


sequencias()