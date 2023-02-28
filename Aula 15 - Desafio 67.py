
while True:
    print('---------------------------------')
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('---------------------------------')
    if num < 0:
        break
    # nao precisa declarara um valor para multi antes nem somar mais 1, pq ele automatiamente ja utiliza os valores no range, mas de 1 a 10
    for multi in range(1, 11):
        print(f'{num} X {multi} = {num*multi}')
print('Tchau!!!')