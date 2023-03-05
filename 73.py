print('Digite o preço do produtos')
a = int(input('Lápis: R$ '))
b = int(input('Borracha: R$ '))
c = int(input('Caderno: R$ '))
d = int(input('Caneta: R$ '))
produtos = ('Lápis', a, 'Borracha', b, 'Caderno', c, 'Caneta', d)
print('=======Listagem de preços=======')
N = 0
while N < 8:
    print(f'{produtos[N]:.<20}R$', end=" ")
    print(f'{produtos[N + 1]:.2f}')
    N += 2
