import time
# // é divisão inteira. Ex: 5/2=2,5 (2 e meio). A divisão inteira é o valor inteiro, ou seja, 2. Então, 5//2=2
# No caixa automático deste banco, o saque é efetuado com o máximo de cédulas com  valores mais altos possível.
saque = 0
print('====================================')
time.sleep(0.2)
print('            BANCO SAULIN            ')
time.sleep(0.2)
print('====================================')
time.sleep(0.2)
saldo = 10000
while True:
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer ver seu saldo? (S/N): ')).upper().strip()[0]
        if resp == 'S':
            print(f'Seu saldo é de R$ {saldo}.')
        saque = int(input('Quanto você quer sacar? R$ '))
        while saque > saldo:
            print('Saldo insuficiente!')
            saque = int(input('Quanto você quer sacar? R$ '))
            while sair not in 'SN':
                sair = str(input('Deseja fazer outra operação? S/N: ')).upper().strip()[0]
            if sair == 'N':
                break
    saldo -= saque
    ced50 = saque // 50
    if ced50 >= 1:
        print(f'Total de {ced50} cédula(s) de R$ 50,00.')
    resto1 = saque - ced50*50
    ced20 = resto1 // 20
    if ced20 >= 1:
        print(f'Total de {ced20} cédula(s) de R$ 20,00.')
    resto2 = resto1 - ced20*20
    ced10 = resto2 // 10
    if ced10 >= 1:
        print(f'Total de {ced10} cédula(s) de R$ 10,00.')
    resto3 = resto2 - ced10*10
    ced1 = resto3
    if ced1 >= 1:
        print(f'Total de {ced1} cédula(s) de R$ 1,00.')
    time.sleep(0.2)
    print('====================================')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja fazer outra operação? S/N: ')).upper().strip()[0]
    if sair == 'N':
        break
print('Obrigado por usar o banco Saulin!')

