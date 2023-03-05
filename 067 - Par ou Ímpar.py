import random

print('Vamos brincar de PAR ou IMPAR! Quando eu ganhar, você pode parar!')
while True:
    pc = random.randint(1, 10)
    # ao contrário do range que não "conta" o último número do range, no randint considera tudo entre 1 e 10.
    num = 0
    while num not in range (1, 11):
        num = int(input(f'Eu já pensei em um número de \033[1;31m1 a 10\033[m em qual você pensou? '))
    oq = ' '
    while oq not in 'PI':
        oq = str(input('Você acha que vai dar par ou ímpar? ')).upper().strip()[0]
    if (pc + num) % 2 == 0:
        if oq == 'P':
            print(f'Eu pensei em {pc}. {pc} + {num} = {pc + num} É par! Perdi!')
        elif oq == 'I':
            print(f'Eu pensei em {pc}. {pc} + {num} = {pc + num} É par! Ganhei!')
            break
    elif (pc + num) % 2 == 1:
        if oq == 'P':
            print(f'Eu pensei em {pc}. {pc} + {num} = {pc + num} É ímpar! Ganhei!')
            break
        elif oq == 'I':
            print(f'Eu pensei em {pc}. {pc} + {num} = {pc + num}. É ímpar! Perdi!')
print('Já que eu ganhei, podemos parar!')


