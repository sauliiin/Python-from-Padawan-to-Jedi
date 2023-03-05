c = 1
while c <= 10:
    print(c)
    #c = c + 1
    c += 1
print('Fim')
print()

print()
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor (0 para parar): '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} pares e {} impares.'.format(par, impar))
print('Fim')
print()