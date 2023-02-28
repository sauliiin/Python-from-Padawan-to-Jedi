# IMPORTANTE!!!!! TESTA PRO CE VER! EU FIZ SÓ COM IF AO INVEZ DE ELIF E REPETIA A MENSAGEM ('Opção INVÁLIDA!') ATE
# QUANDO TAVA CERTO

escolha = 0
print('DIGITE 2 VALORES!')
n1 = int(input('Digite o primeiro: '))
n2 = int(input('Digite o segundo: '))
print('=+=' * 8)
print('ESCOLHA UMAS DAS OPÇÕES ABAIXO\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] RECOMEÇAR\n[5] SAIR ')
while escolha != 5:
    escolha = int(input('Qual a sua opção: '))
    if escolha == 4:
        print('=+='*8)
        print('DIGITE 2 VALORES!')
        n1 = int(input('Digite o primeiro: '))
        n2 = int(input('Digite o segundo: '))
        print('ESCOLHA UMAS DAS OPÇÕES ABAIXO\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] RECOMEÇAR\n[5] SAIR ')
    elif escolha == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif escolha == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        elif n1 < n2:
            print(f'{n2} > {n1}')
        else:
            print('OS VALORES SAO IGUAIS')
    else:
        print('Opção INVÁLIDA!')
print('SAINDO!')
