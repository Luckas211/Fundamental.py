texto = "Lucas"
iteratador = iter(texto)

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break
