lista = [int(input('Digite um valor: ')),
         int(input('Otro: ')),
         int(input('Mais um: ')),
         int(input('O último: '))]
print(lista)
print(f'Os valores digitados foram {lista}.')
print(f'O maior digitado foi {max(lista)} que está na posição {lista.index(max(lista))}.')
print(f'O menor digitado foi {min(lista)} que está na posição {lista.index(min(lista))}.')

