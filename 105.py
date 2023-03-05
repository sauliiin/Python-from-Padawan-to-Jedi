from pacotes import funcoes


def area(l, c):
    print(f'A área do seu terro de {l}m x {c}m é de {l * c}m².')


while True:
    l = float(input('Digite a largura do terreno: '))
    c = float(input('Digite o comprimento do terreno: '))
    area(l, c)
    while True:
        resp = funcoes.simnao('Deseja continuar? (S/N) ')
        if resp in 'SN':
            break
    if resp == 'N':
        break
