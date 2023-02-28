import math

maiorpeso = 0
menorpeso = math.inf
for cont in range(0, 5):
    nome = str(input('Qual o seu nome: ')).strip().title()
    peso = float(input('Qual o seu peso? '))
    if peso > maiorpeso:
        maiorpeso = peso
        gordao = nome
    if peso < menorpeso:
        menorpeso = peso
        magrin = nome
print('{} é o gordão da turma com {}kg.'.format(gordao, maiorpeso))
print('{} é o magrin da turma com {}kg.'.format(magrin, menorpeso))