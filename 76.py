import random

tupla = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
print(f'Estes são 5 números aletatórios {tupla}')
print(f'Este é o menor: {(sorted(tupla)[0])}.')
print(f'Este é o maior: {(sorted(tupla)[-1:])}.')
print(f'Este é o menor: {(min(tupla))}.')
print(f'Este é o maior: {(max(tupla))}.')