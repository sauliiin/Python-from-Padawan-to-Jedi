

tupla = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    numero = int(input('Digite um número entre 1 e 10: '))
    if 0 < numero <= 10:
        print(f'O número digitado por extenso é: {tupla[numero - 1]}.')
        break



