'''def generator(n=0):
    yield 1
    print("Continuando")
    yield 2

gen = generator(n=0)

print(next(gen))
print(next(gen))'''

# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)