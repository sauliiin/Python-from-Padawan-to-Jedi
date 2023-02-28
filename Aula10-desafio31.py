#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#FIZ MAIS DIFICIL: Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km,ACIMA DESSA DISTANCIA, R$0,45.
import time

distancia = float(input('Qual a distancia percorrida na viagem? '))
print('Como você percorreu {:.2f} km, você deve pagar o valor abaixo:'.format(distancia))
print('\33[1;31;46m...PROCESSANDO...\033[m' * 5)
time.sleep(3)
if distancia <= 200.00:
    print("Voce deve pagar R$ {:.2f}.".format(distancia*0.50))
else:
    valor = distancia - 200.00
    dinheiro = valor*0.45
    total = 200*0.5+dinheiro
    print("Você vai pagar R$ {}".format(total))
