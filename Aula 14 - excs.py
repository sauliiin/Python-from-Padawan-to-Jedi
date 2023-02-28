c = 1
while c <= 10:
    print(c)
    #c = c + 1
    c += 1
print('Fim')
print()
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
print()
resposta = 'SIM'
while resposta == 'SIM':
    n = int(input('Digite um valor: '))
    resposta = str(input('Deseja continuar? ')).upper().strip()
print('Fim')
print()
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digito {} pares e {} impares.'.format(par, impar))
print('Fim')
print()