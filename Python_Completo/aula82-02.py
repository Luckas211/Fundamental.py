def executa(funcao, *args):
    return funcao(*args)

somar = lambda x,y: x+y

print(somar(2,3))

multiplicar = lambda m: lambda n: n * m
resultado = multiplicar(2)

print(resultado(2))

duplica = executa(lambda x: lambda y: x * y, 2)
print(duplica(5))