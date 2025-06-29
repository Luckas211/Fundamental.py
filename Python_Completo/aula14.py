a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
print(formato)

n1 = "Lucas"
n2 = "Silva"
juntos = 'nome:{ler1},sobrenome:{ler2}'
resultado = juntos.format(
    ler1=n1, ler2=n2
    )
print(resultado)