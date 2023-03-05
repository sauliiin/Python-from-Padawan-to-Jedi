palavras = ('biscoito', 'bola', 'cabelo', 'trem')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as seguintes vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
