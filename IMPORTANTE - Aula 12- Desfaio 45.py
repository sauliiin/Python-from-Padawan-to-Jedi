import time
import emoji
import random

vitoriapc = 0
print(emoji.emojize('Vamos jogar :rock: ou :scroll: ou :scissors:?', language='alias'))
while vitoriapc == 0:
    escolha = (str(input('Eu já pensei na minha opção, agora escreva a sua: PEDRA, PAPEL OU TESOURA? '))).upper().strip()
    while escolha != 'PEDRA' and escolha != 'PAPEL' and escolha != 'TESOURA':
        print('**************')
        time.sleep(0.3)
        print('OPÇÃO INVÁLIDA')
        time.sleep(0.3)
        print('**************')
        time.sleep(0.3)
        escolha = (str(input('POR FAVOR, vamos brincar! Eu já pensei na minha opção, qual a sua: PEDRA, PAPEL OU TESOURA? '))).upper().strip()
    print('**************')
    time.sleep(1)
    print('J O K E N P Ô')
    time.sleep(1)
    print('**************')
    time.sleep(1)
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = random.choice(lista)
    print('Eu pensei em {}.'.format(computador), end=" ")
    if computador == 'TESOURA' and escolha == 'PEDRA':
        vitoriapc += 1
        print(emoji.emojize(':rock: ganha de :scissors:, eu GANHEIII!!! Hahaha :beaming_face_with_smiling_eyes:', language='alias'))
    elif computador == 'PEDRA' and escolha == 'TESOURA':
        print(emoji.emojize(':rock: ganha de :scissors:, você ganhou! :cry:', language='alias'))
        print('Vamos jogar de novo!!!!')
        time.sleep(2)
    elif computador == 'PAPEL' and escolha == 'TESOURA':
        print(emoji.emojize(':scissors: ganha de :scroll:, você ganhou! :cry:', language='alias'))
        print('Vamos jogar de novo!!!!')
        time.sleep(2)
    elif computador == 'TESOURA' and escolha == 'PAPEL':
        vitoriapc += 1
        print(emoji.emojize(':scissors: ganha de :scroll:, eu GANHEIII!!! Hahaha :beaming_face_with_smiling_eyes:', language='alias'))
    elif computador == 'PEDRA' and escolha == 'PAPEL':
        print(emoji.emojize(':scroll: ganha de :rock:, você ganhou! :cry:', language='alias'))
        print('Vamos jogar de novo!!!!')
        time.sleep(2)
    elif computador == 'PAPEL' and escolha == 'PEDRA':
        vitoriapc += 1
        print(emoji.emojize(':scroll: ganha de :rock:, eu GANHEIII!!! Hahaha :beaming_face_with_smiling_eyes:', language='alias'))
    else:
        print('EMPATE! Vamos jogar de novo!!!!')
        time.sleep(2)


