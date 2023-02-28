print("Você ganhou um item da lista abaixo, que será soteado!")
import random
print('Biscoito, Chocolate, R$ 100,00 e Playstation, qual será seu prêmio?')
n1 = 'Biscoito'
n2 = 'Chocolate'
n3 = 'R$ 100,00'
n4 = 'Playstation'
lista = [n1, n2, n3, n4]
n5 = random.choice(lista)
print('O prêmio sorteado é {}.'.format(n5))

print("Você ganhou um item da lista abaixo, que será soteado!")
import random
print('Biscoito, Chocolate, R$ 100,00 e Playstation, qual será seu prêmio?')
lista = ['Biscoito', 'Chocolate', 'R$ 100,00', 'Playstation']
n5 = random.choice(lista)
print('O prêmio sorteado é {}.'.format(n5))

print('Um de quatro alunos serão sorteados')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo nome: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista2 = [a1, a2, a3, a4]
a5 = random.choice(lista2)
print('O escolhido foi:', a5)