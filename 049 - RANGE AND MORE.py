import time
import emoji

# Se eu quero um range entre 1 e 10, devo colocar for cont in range (1, 11) pq o último número não conta.
for cont in range(10, -1, -1):
    print(cont)
    time.sleep(0.5)
print('Boooommmm!')
time.sleep(0.5)
print(emoji.emojize(':fireworks:'*5))
print()

for cont in range(1, 10, 2):
    print(cont)
    time.sleep(0.5)
print('Boooommmm!')
time.sleep(0.5)
print(emoji.emojize(':fireworks:'*5))
print()

for cont in range(1, 10):
    print(cont)
    time.sleep(0.5)
print('Boooommmm!')
time.sleep(0.5)
print(emoji.emojize(':fireworks:'*5))
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
# s = s + n pode ser representado no Python na forma abaixo
    s += n
print('O somatório dos valores digitados é: {}.'.format(s))
