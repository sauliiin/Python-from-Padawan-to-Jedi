print('Faça um programa que leia um número entre 0 a 9999 e mostre na tela cada um dos dígitos separados')
num = int(input('Digite um número entre 1000 e 9999: '))
nome = str(num)
print('A unidade é {}.'.format(nome[3]))
print('A dezena é {}.'.format(nome[2]))
print('A centena é {}.'.format(nome[1]))
print('A milhar é {}.'.format(nome[0]))

print('Agora, faça um programa que leia um número entre 0 a 9999 e mostre na tela cada um dos dígitos separados')
num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade é {}.'.format(u))
print('A dezena é {}.'.format(d))
print('A centena é {}.'.format(c))
print('A milhar é {}.'.format(m))
