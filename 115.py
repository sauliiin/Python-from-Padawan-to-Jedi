from time import sleep
pessoa = {}
time = []


def dados(a, b, c, d):
    if a == '':
        a = '<desconhecido>'
    if b == '':
        b = '<não informada>'
    if c == '':
        c = '<não informado>'
    if d == '':
        d = 0
    print(f'O candidato {a}, idade {b}, sexo {c}, alcançou {d} ponto(s).')


print('-=' * 15)
cont = int(input('Deseja cadastrar quantas pessoas? '))
for cont in range(0, cont):
    pessoa['Nome'] = str(input('Digite o nome: ')).strip().title()
    pessoa['Idade'] = str(input('Qual a idade? '))
    pessoa['Sexo'] = str(input('Qual o sexo? (M/F) ')).upper().strip()
    pessoa['Pontuação'] = str(input('Qual a pontuação? '))
    print('-=' * 15)
    time.append(pessoa.copy())
print(time)
print('-=' * 15)
print(f'{"Nº":<3}{"Nome":<10}{"Pontuação":^5}')
sleep(0.5)
for cont in range(0, cont + 1):
    print(f'{cont + 1:<3}{time[cont]["Nome"]:<10}{str(time[cont]["Pontuação"]):^5}')
    sleep(0.5)
print('-=' * 15)
while True:
    n = int(input('Informe o número do candidato que você quer obter mais informações: '))
    dados(time[n-1]['Nome'], time[n-1]['Idade'], time[n-1]['Sexo'], time[n-1]['Pontuação'])
    while True:
        resp = str(input('Deseja mais informações? (S/N) ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N!')
    if resp == 'N':
        break
