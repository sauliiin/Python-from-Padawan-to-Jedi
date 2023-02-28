from random import randint
from time import sleep
from operator import itemgetter
cont = 1
participantes = {}
for c in range(1, 5):
    jogada = randint(1, 6)
    participantes[f'Jogador {c}'] = jogada
    print(f'O jogador {c} tirou {jogada}')
    sleep(1)
print(participantes)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
ordem = sorted(participantes.items(), key=itemgetter(1), reverse=True)
# ou, seu eu quiser que a ordem fique em um dicionário: ordem = dict(sorted(participantes.items(), key=lambda item: item[1], reverse=True))
# mas ai o enumerate nao funciona, teria que ser o ordem.items():
print(ordem)
for indice, valor in enumerate(ordem):
    print(valor)
    print(f'{indice + 1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)