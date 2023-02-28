from math import sqrt, floor, ceil
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

'Em comparaçao ao Ex 1 da aula 8, se eu importo, não preciso escrever math  toda vez, ' \
'pq ele já vai presumir que eu quero é a raiz quadrada - sqrt '