"""lista = [n+1 for n in range(10)]
print(lista)
print()
print()
generator = (numeros for numeros in range(10))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))"""

import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)