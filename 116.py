def check_input(n):
    try:
        teste = int(n)
        print(f'Você digitou o número inteiro {teste}.')
    except ValueError:
        try:
            teste = float(n)
            print(f'\033[0;31mVocê digitou um valor flutuante {teste}.\033[m')
        except ValueError:
            print(f'\033[0;31mNão.. O dado digitado é uma string: {n}.\033[m')


num = ''
while num != '999':
    num = input('Digite um número [999 para PARAR]: ')
    check_input(num)

