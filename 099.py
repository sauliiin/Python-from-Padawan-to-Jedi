from random import randint
from time import sleep

cont = 1
participantes = {}
for c in range(1, 5):
    jogada = randint(1, 6)
    participantes[f'Jogador {c}'] = jogada
    print(f'O jogador {c} tirou {jogada}')
    sleep(1)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
ordem = dict(sorted(participantes.items(), key=lambda item: item[1], reverse=True))
#{'Jogador 1': 6, 'Jogador 2': 2, 'Jogador 3': 4, 'Jogador 4': 6}
#para a chave 'Jogador 1' o valor é 6
for k, v in ordem.items():
    print(f'{cont}º lugar: {k} com {v}.')
    cont += 1
    sleep(1)
print(participantes)
