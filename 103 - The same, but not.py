import time
aproveitamento = {}
porjogo = []
geral = []

while True:
    aproveitamento['Nome'] = str(input('Digite o nome do jogador: ')).title().strip()
    aproveitamento['Jogos'] = int(input('Em quantos jogos ele participou? '))
    for c in range(1, aproveitamento['Jogos'] + 1):
        porjogo.append(int(input(f'Quantos gols ele fez na partida {c}? ')))
    aproveitamento['Gols por jogo'] = porjogo[:]
    aproveitamento['Total de gols no campeonato'] = sum(porjogo)
    geral.append(aproveitamento.copy())
    porjogo.clear()
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N!')
    if resp == 'N':
        break
    print('-='*15)
print('-='*15)
time.sleep(1)
print(f'{"Nº":<3}{"NOME":<10}{"TOTAL":<9}{"POR JOGO":^5}')
time.sleep(1)
for cont in range(0, len(geral)):
    print(f'{(cont + 1):<3}{geral[cont]["Nome"]:<12}{geral[cont]["Total de gols no campeonato"]:<7}{geral[cont]["Gols por jogo"]}')
    time.sleep(1)
print('-=' * 15)
while True:
    resp2 = int(input('Deseja mais informações de qual jogador? '))
    time.sleep(1)
    for cont in range(0, geral[resp2 - 1]['Jogos']):
        print(f'Na partida {cont + 1}, o {geral[resp2 - 1]["Nome"]} fez {geral[resp2 - 1]["Gols por jogo"][cont]} gol(s).')
        time.sleep(1)
    print('-=' * 15)
    perg2 = ' '
    while perg2 not in 'SN':
        perg2 = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
    if perg2 == 'N':
        break
print('-='*15)


