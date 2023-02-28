import time
from pacotes import texto

while True:
    texto.titulo('COMPRA ONLINE')
    preco = float(input('Olá! Me informe o preço do produto. R$ '))
    # Para nao ter que escrever print várias vezes em cada linha é só usar 3 '''
    print('''Por favor, escolha uma das formas de pagamento abaixo:
    [1] - À vista no dinheiro ou PIX com 10% de desconto
    [2] - À vista no cartão de crédito com 5% de desconto
    [3] - Parcelado em 2x sem juros
    [4] - Parcelado em 3x ou mais com 20% de juros''')
    resposta = int(input('Qual sua opção: '))
    while resposta != 1 and resposta != 2 and resposta != 3 and resposta != 4:
            texto.atencao('OPÇÃO INVÁLIDA!')
            resposta = int(input('Qual sua opção: '))
    if resposta == 1:
        print('O valor para pagamento é de R$ {:.2f}.'.format(preco*0.9))
    elif resposta == 2:
        print('O valor para pagamento é de R$ {:.2f}.'.format(preco*0.95))
    elif resposta == 3:
        print('O valor para pagamento será de 2 parcelas de R$ {:.2f}.'.format(preco/2))
    elif resposta == 4:
        parcelas = (int(input('Em quantas parcelas você quer dividir? ')))
        print('O valor de cada parcela será de R${:.2f}.'.format((preco/parcelas)*1.2))
    opcao = input('Desjea continuar? S/N ').upper().strip()
    if opcao == 'N':
        break