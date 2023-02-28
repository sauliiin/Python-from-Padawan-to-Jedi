def inteiro(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except (ValueError, TypeError):
            print(f'\033[0;31mO dado informado é inválido! Por favor, digite um NÚMERO INTEIRO.\033[m')


def simnao(msg):
    while True:
        try:
            n = input(msg).strip().upper()
            if n in 'SN':
                return n
            else:
                print(f'\033[0;31mPor favor, digite S ou N.\033[m')
        except (ValueError, TypeError):
            print('Não foi mpossível validar sua resposta!')


resp = soma = cont = maior = menor = 0
while resp != 'N':
    n = inteiro('Digite um número inteiro: ')
    resp = str(simnao('Deseja continuar (S/N) '))
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if menor == 0 or n < menor:
            menor = n
print(f'O maior número é {maior}, o menor {menor}, a soma de todos os números {cont} digitadoes é {soma} e a média entre eles é {soma/cont}')