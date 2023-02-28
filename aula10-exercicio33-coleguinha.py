n1 =int(input('Digite o primeiro número:  '))
n2 =int(input('Digite o segundo número: '))
n3 =int(input ('Digite o terceiro número: '))

lista =[n1,n2,n3]
lista_ordenada = sorted(lista)
print(len(lista))
print('O menor número é {}'.format(lista_ordenada[0]))
print ('O maior número é {}'.format(lista_ordenada[2]))
print (f'O maior número é {lista_ordenada[len(lista) - 1]}')
