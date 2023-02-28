from time import sleep
def linhas():
    print('-='*20)


linhas()
print('Contagem de 1 até 10, de 1 em 1:')
for cont in range(1, 11, 1):
    print(f'{cont} -> ', end='')
    sleep(0.5)
print('Booom!')
linhas()
print('Contagem de 10 até 0, de 2 em 2:')
for cont in range(10, -1, -2):
    print(f'{cont} -> ', end='')
    sleep(0.5)
print('Booom!')
linhas()
print('Agora é a sua vez de personalizar a contagem! ')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
if n2 > n1:
    for cont in range(n1, n2 +1, n3):
        print(f'{cont} -> ', end='')
        sleep(0.5)
elif n1 > n2 and n3 > 0:
    n4 = n3 * -1
    for cont in range(n1, n2 -1, n4):
        print(f'{cont} -> ', end='')
        sleep(0.5)
elif n1 > n2 and n3 < 0:
    for cont in range(n1, n2 -1, n3):
        print(f'{cont} -> ', end='')
        sleep(0.5)
elif n3 == 0:
    if n2 > n1:
        for cont in range(n1, n2 + 1, 1):
            print(f'{cont} -> ', end='')
            sleep(0.5)
    elif n1 > n2:
        for cont in range(n1, n2 - 1, -1):
            print(f'{cont} -> ', end='')
            sleep(0.5)
print('Booom!')
