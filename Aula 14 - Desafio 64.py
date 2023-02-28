from pacotes import texto

def check_input(n):
    try:
        teste = int(n)
        print(f'Você digitou o número inteiro {teste}.')
    except ValueError:
        try:
            teste = float(n)
            print(f'Você digitou o valor flutuante {teste}.')
        except ValueError:
            texto.atencao(f'Não.. O dado digitado é uma string: {n}.')


num = ''
while num != '999':
    num = input('Digite um número [999 para PARAR]: ')
    check_input(num)
