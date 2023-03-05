lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[0:3])
print(lanche[1:])
print(lanche[-3])


for comida in lanche:
    print(f'Eu vou comer {comida}')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

print(sorted(lanche))
