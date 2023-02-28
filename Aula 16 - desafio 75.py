a = int(input('Digite um número: '))
b = int(input('Outro: '))
c = int(input('Mais um: '))
d = int(input('O último: '))
tupla = (a, b, c, d)
print(f'Os números digitados foram: {tupla}')
if tupla.count(9) > 0:
    print(f'O 9 apareceu {tupla.count(9)} vez(es)')
else:
    print('O número 9 não foi digitado.')
if tupla.count(3) > 0:
    print(f'O número 3 foi digitado na {tupla.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado')
print('Foram digitados este(s) número(s) par(es):', end=" ")
for cont in tupla:
    if cont % 2 == 0:
        print(cont, end=" ")
#para quebrar a linha é o comando: \n