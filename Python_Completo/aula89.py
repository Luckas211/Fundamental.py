# Definindo uma string
string = "Hello, World!"

# Método que queremos verificar e acessar
metodo = "upper"

# Verificando se a string possui o método especificado
if hasattr(string, metodo):
    # Se o método existir, obter e chamar o método
    metodo_upper = getattr(string, metodo)
    resultado = metodo_upper()
    print(f"O método '{metodo}' existe e seu resultado é: {resultado}")
else:
    print(f"O método '{metodo}' não existe na string.")

