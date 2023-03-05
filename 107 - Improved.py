from time import sleep


def linhas():
    print('-=' * 20)


def contagem(a, b, c):
    if b > a:
        for cont in range(a, b + 1, c):
            print(f'{cont} -> ', end='')
            sleep(0.5)
    elif a > b and c > 0:
        d = c * -1
        for cont in range(a, b - 1, d):
            print(f'{cont} -> ', end='')
            sleep(0.5)
    elif a > b and c < 0:
        for cont in range(a, b - 1, c):
            print(f'{cont} -> ', end='')
            sleep(0.5)
    elif c == 0:
        if b > a:
            for cont in range(a, b + 1, 1):
                print(f'{cont} -> ', end='')
                sleep(0.5)
        elif a > b:
            for cont in range(n1, n2 - 1, -1):
                print(f'{cont} -> ', end='')
                sleep(0.5)


print(contagem(1, 10, 1))
linhas()
print(contagem(10, 0, -1))
linhas()
print('Agora é a sua vez de personalizar a contagem! ')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
n4 = int(input('Passo: '))
if n4 == 0:
    if n2 > n1:
        n3 = 1
    elif n1 > n2:
        n3 = -1
else:
    n3 = n4
contagem(n1, n2, n3)
