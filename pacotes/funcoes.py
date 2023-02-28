# VALIDAR NUMERO DIGITADO COM VIRGULA, COM ESPAÇO. PARA INT E FLOAT?
# Try, vc tenta uma operação. Se falhar, except


#def validacao(n: str) -> int:
def validacao(n):
    a = str(n).replace(",", ".")
    try:
        teste = int(a)
        print(f'Você digitou o número inteiro {teste}.')
    except ValueError:
        try:
            teste = float(a)
            print(f'\033[0;31mVocê digitou o valor real {teste}.\033[m')
        except ValueError:
            print(f'\033[0;31mNão.. O dado digitado é uma string: {a}.\033[m')


def num(n):
    global a
    a = str(n).replace(",", ".")
    try:
        teste = int(a)
        return a
    except ValueError:
        try:
            teste = float(a)
            return a
        except ValueError:
            print(f'\033[0;31mErro! O dado digitado é uma string: {a}.\033[m')


def inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mO dado informado é inválido! Por favor, digite um NÚMERO INTEIRO.\033[m')
            continue
# O CONTINUE JÁ DEVOLVE PARA O WHILE NO INICIO!!!!! PORRAAAAMMM
        else:
            return n


def simnao(msg):
    while True:
        try:
            r = input(msg).strip().upper()
            if r == "":
                print('\033[0;31mPor favor, digite S ou N.\033[m')
                continue
            if r in 'SN':
                return r
            else:
                print(f'\033[0;31mPor favor, digite S ou N.\033[m')
        except (ValueError, TypeError):
            print('Não foi mpossível validar sua resposta!')