from random import randint
lista = []
print('-'*20)
print('    JOGOS NA MEGA    ')
print('-'*20)
n = int(input('Quantos jogos aletatórios você quer sortear? '))
for c in range(1, n+1):
    print(f'Jogo {c}: ', end='')
    for cont in range(0, 6):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
    lista.sort()
    print(lista)
    lista.clear()


