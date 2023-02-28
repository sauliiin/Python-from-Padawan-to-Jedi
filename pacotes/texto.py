def verm(msg):
    print(f'\033[1;31m{msg}\033[m')


def atencao(msg):
    print(f'\033[1;30;41m{msg}\033[m')


def azul(msg):
    print(f'\033[1;34m{msg}\033[m')


def amarelo(msg):
    print(f'\033[1;33m{msg}\033[m')


def titulo(msg):
    print('\033[1m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
    print(f'\033[1m{msg:^30}\033[m')
    print('\033[1m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')


def linha():
    print('\033[1m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')


