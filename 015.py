import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Dicas de import

import math
num = float(input('Digite um número qualquer com dígitos depois do ponto: '))
print('O número inteiro é {}'.format(math.trunc(num)))

from math import trunc
num = float(input('Digite um número: '))
print('O número inteiro é {}'.format(trunc(num)))

num = float(input('Digite um número: '))
print('O número inteiro é {}'.format(int(num)))

#Quando vc coloca o ponto depois do math, ele vai trazer tudo que tem em math'
