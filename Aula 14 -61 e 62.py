print('========================')
print(' PROGRESSÃO ARITIMÉTICA ')
print('========================')
numero = int(input('Digite o primeiro termo: '))
razao = int(input('Digite razão atirimética? '))
contador = 0
while contador < 10:
    print('{} -> '.format(numero), end='')
    numero = numero + razao
    contador = contador + 1
print('ACABOU!')
opcao = 1
while opcao != 0:
    opcao = int(input('Você quer ver mais quantos termos? '))
    contador = 0
    while contador < opcao:
        print('{} -> '.format(numero), end='')
        numero = numero + razao
        contador = contador + 1
print('ACABOU!')