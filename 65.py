while True:
    print('---------------------------------')
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('---------------------------------')
    # nao precisa declarara um valor para multi antes nem somar mais 1, pq ele automaticamente ja utiliza os valores no range, mas de 1 a 10
    for multi in range(1, 11):
        print(f'{num} X {multi} = {num*multi}')
    resp = input('Deseja continuar? (S/N) ').strip().upper()[0]
    if resp in 'Nn':
        break
print('Tchau!!!')