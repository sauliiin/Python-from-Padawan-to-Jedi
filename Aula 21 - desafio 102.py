def fatorial(num, calc=False):
    """
    :param num: Faz referência ao número do qual quero calcular o fatorial
    :param calc: Dá o retorno se mostra ou não os cálculos
    :índice: f *= cont é o mesmo que f = f * cont
             cont -= 1 é o mesmo que cont = cont -1
    :return: mostar o fatorial de um número
    """
    cont = num
    f = 1
    if calc is True:
        print(f'Calculando {n}! -> ', end='')
        while cont > 0:
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
            f *= cont
            cont -= 1
        print(f'{f}')
    else:
        while cont > 0:
            f = f * cont
            cont -= 1
        print(f'O fatorial de {num} é {f}.')


help(fatorial)
while True:
    n = int(input('Você quer saber o fatorial de qual número? '))
    b = str(input('Você quer ver os cálculos? (S/N) ')).upper().strip()[0]
    if b in 'S':
        show = True
    else:
        show = False
    fatorial(n, show)
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N!')
    if resp == 'N':
        break


