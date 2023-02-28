from math import factorial
numero = int(input('Digite um valor para saber o seu fatorial: '))
print('Ex: 5x4x3x2x1=120')
fatorial = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, fatorial))

numero = int(input('Digite um valor para saber o seu fatorial: '))
contador = numero
fatorial = 1
#for contador in range(numero, 0, -1):
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    #fatorial = fatorial * contador
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))