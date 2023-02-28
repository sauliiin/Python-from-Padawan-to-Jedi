import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

'Quando vc coloca o ponto depois do math, ele vai trazer tudo que tem em math'
