from random import randint
erros = 0
tentativa = 0
numero = randint(0, 20)
print('Eu pensei em um número, vamos ver quanto vc demora para adivinhar...')
while tentativa != numero:
# while not tentativa = numero
    tentativa = int(input('Digite o número de 0 a 20 que vc acha que eu pensei: '))
    erros += 1
    if tentativa == numero:
        print('Acertou mizeravi!')
    else:
        if tentativa > numero:
            print('É um pouco menor...')
        elif tentativa < numero:
            print('É um pouco maior...')
print(f'Você precisou chutar {erros} vez(es) para adivinhar!')