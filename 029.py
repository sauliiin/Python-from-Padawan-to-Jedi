#Escreva um programa que faça o PC pensar em um número inteiro entre 0 e 5 e peça para o usuário adivinhar. O programa deve escrever se venceu ou perdeu.
import time

nome = str(input('Olá! Qual é seu nome? ')).strip().title()
print('-=-'*20)
print('Muito prazer em te conhecer, {}!' .format(nome))
print('-=-'*20)

fatiar = nome.split()
primeiro = (fatiar[0])
#Isso acima é só pra chamar a pessoa pelo primeiro nome

import random
#poderia colocar: from random import randint
num = random.randint(1, 5)
tentativa = int(input('Digite um número inteiro entre 0 e 5: '))
print('-=-'*20)
print('PROCESSANDO...')
time.sleep(2)
#interessante, que eu escrevi só import time antes e o pycharm ficou resistente... só que depois que eu coloquei o time.sleep ele importou o time sozin
print('-=-'*20)
if tentativa == num:
    print("Parábens, {}, você acertou o número!".format(primeiro))
else:
    print("Que pena {}, eu pensei no número {}, melhor sorte da próxima vez!".format(primeiro, num))

