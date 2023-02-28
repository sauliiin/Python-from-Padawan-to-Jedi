#Escreva um programa que você digita a velocidade de uma carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

import time

velocidade = float(input("O seu veículo estava a quantos Km/h? "))
if velocidade <= 80.00:
    print('Prossiga com cautela!')
else:
    print('Ixi...Você foi multado!')
    print('-Processando-'*5)
    time.sleep(3)
    #pmulta = velocidade-80.00
    #multa = pmulta*7
    multa = (velocidade-80)*7
    print('Você foi multado em R${:.2f}.'.format(multa))

