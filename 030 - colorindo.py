# Sempre que vc quiser utilizar uma cor no python, vc vai utilizar esse código \033[ ; ; m
# vamos lá: \33[0;33;44m .
#0 = Sem estilo - A cores do texto vão de 30 a 37: branco 30, vermelho 31, verde 32, am, 33, az 34, roxo 35, calcinha 36, cinza 37
#1 = Negrito    - A cores de fundo vão de 40 a 47: branco 40, vermelho 41, verde 42, am, 43, az 44, roxo 45, calcinha 46, cinza 47
#4 = Sublinhado
#7 = Negativo (fundo e letra com cores invertidas)
#\033[m]   Assim volta pro padrão do terminal, preto e branco.
#\033[7:30m Assim inverte e faz a letra preta com fundo branco!

print('\033[31mOlá Mundo!\033[m')

# #Escreva um programa que você digita a velocidade de uma carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

import time

velocidade = float(input("O seu veículo estava a quantos Km/h? "))
if velocidade <= 80.00:
    print('\033[4;30;45mProssiga com cautela 🙂!\033[m')
else:
    print('\033[1;31;40mIxi...Você foi multado!\033[m')
    print('-Processando-'*5)
    time.sleep(3)
    #pmulta = velocidade-80.00
    #multa = pmulta*7
    multa = (velocidade-80)*7
    print('Você foi multado em \033[1;31;43m R${:.2f}.\033[m'.format(multa))

#Outra forma!!!!
print('Você estava a {}{:.2f}{} km/h'.format('\033[4;34m', velocidade, '\033[m'))
