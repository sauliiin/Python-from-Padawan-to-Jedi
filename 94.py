ficha = []
while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('-='*15)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>9}')
print('-='*15)
print(ficha)
for i, a in enumerate(ficha):
#for posição, valor in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.2f}')
print('-='*15)
while True:
    resp = int(input('Deseja ver as notas parciais de qual aluno? '))
    print(ficha[resp - 1][0], ':', ficha[resp - 1][1], '.')
    perg2 = ' '
    while perg2 not in 'SN':
        perg2 = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
    if perg2 == 'N':
        break