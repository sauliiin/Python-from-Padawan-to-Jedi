soma = 0
for cont in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print('A soma dos valores pares é {}.'.format(soma))
