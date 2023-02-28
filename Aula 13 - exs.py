import time

for cont in range(0, 6):
    print(cont)
print('Fim')
print()

for cont in range(6, 0, -1):
    print(cont)
print('Fim')
print()

for cont in range(0, 10, 2):
    print(cont)
print('Fim')
print()

n = int(input('Digite um número: '))
for cont in range(0, n+1):
    print(cont)
    time.sleep(0.5)
print('FIM')
print()

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for cont in range(inicio, fim+1, passo):
    print(cont)
    time.sleep(0.5)
print('FIM')
print()

s = 0
for cont in range(0, 3):
    n = int(input('Digite um valor: '))
# s = s + n pode ser repesentado no phyton na forma abaixo
    s += n
print('O somátório dos valores digitados é: {}.'.format(s))
