import time
lista = []
ordem = 0
while True:
        ordem += 1
        nome = str(input('Nome do aluno: ')).title().strip()
        n1 = float(input('Nota 1: '))
        n2 = float(input('Nota 2: '))
        m = (n1 + n2)/2
        lista.append([nome, [n1, n2], m])
        perg = ' '
        while perg not in 'SN':
            perg = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
        if perg == 'N':
            break
print('-='*20)
time.sleep(0.5)
print(f'{"Nº":<5}{"NOME":<8}{"MÉDIA":^10}')
for cont in range(0, ordem):
        print(f'{cont + 1:<5}{lista[0 + cont][0]:<8}{lista[0 + cont][2]:^10.2f}')
        time.sleep(0.5)
print('-='*20)
time.sleep(0.5)
while True:
        resp = int(input('Deseja ver as notas parciais de qual aluno? '))
        print(lista[resp - 1][0], ':', lista[resp - 1][1])
        perg2 = ' '
        while perg2 not in 'SN':
                perg2 = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
        if perg2 == 'N':
                break
