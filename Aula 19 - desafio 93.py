aproveitamento = {}
porjogo = []

aproveitamento['Nome'] = str(input('Digite o nome do jogador: ')).title().strip()
aproveitamento['Jogos'] = int(input('Em quantos jogos ele participou? '))
for c in range(1, aproveitamento['Jogos'] + 1):
    porjogo.append(int(input(f'Quantos gols ele fez na partida {c}? ')))
aproveitamento['Gols por jogo'] = porjogo[:]
aproveitamento['Total de gols no campeonato'] = sum(porjogo)
print(aproveitamento)
print(porjogo)
print('-='*15)
for key, value in aproveitamento.items():
    print(f'{key}: {value}.')
print('-='*15)
print(f'O jogador {aproveitamento["Nome"]} participou de {aproveitamento["Jogos"]} jogo(s).')
for cont in range(0, aproveitamento['Jogos']):
    print(f'Na partida {cont + 1} ele fez {porjogo[cont]} gol(s).')