a = b = c = d = e = f = g = maior = soma = somapares = 0
lista = list()
pares = list()
listona = list()
while a < 3:
    n = int(input(f'Digite um valor para [0, {a}]: '))
    if n % 2 == 0:
        somapares += n
        pares.append(n)
    lista.append(n)
    a += 1
listona.append(lista[:])
lista.clear()
while b < 3:
    n = int(input(f'Digite um valor para [1, {b}]: '))
    if n % 2 == 0:
        somapares += n
        pares.append(n)
    if n > maior:
        maior = n
    lista.append(n)
    b += 1
listona.append(lista[:])
lista.clear()
while c < 3:
    n = int(input(f'Digite um valor para [2, {c}]: '))
    soma += n
    if n % 2 == 0:
        somapares += n
        pares.append(n)
    lista.append(n)
    c += 1
listona.append(lista[:])
lista.clear()
print('=*'*15)
while d < 3:
    print(f'[ {listona[0][d]} ]', end='')
    d += 1
print('\n')
while e < 3:
    print(f'[ {listona[1][e]} ]', end='')
    e += 1
print('\n')
while f < 3:
    print(f'[ {listona[2][f]} ]', end='')
    f += 1
print('\n')
print('=*'*15)
print(f'Os valores pares digitados são: {pares} e a sua soma é: {somapares}.')
print(f'A soma dos valores da terceira coluna é: {soma}.')
print(f'O maior valor da segunda linha é: {maior}.')
