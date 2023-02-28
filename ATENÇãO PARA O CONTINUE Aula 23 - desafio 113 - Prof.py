from pacotes import funcoes

def inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mO dado informado é inválido! Por favor, digite um NÚMERO INTEIRO.\033[m')
            continue
# O CONTINUE JÁ DEVOLVE PARA O WHILE NO INICIO!!!!! PORRAAAAMMM
        except (KeyboardInterrupt):
            print('O usuário INTERROMPEU a operação.')
            return 0
        else:
            return n


num = inteiro('Digite um valor: ')
funcoes.inteiro('Digite um valor: ')