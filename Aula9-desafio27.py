print('Faça um porgrama que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separados')
nome = str(input('Digite o seu nome completo: ')).strip().title()
print('Muito prazer em te conhecer,', nome)
print(f'Posso te chamar apenas de {nome.split()[0]}?')
fatiar = nome.split()
print(fatiar)
print('Seu primeiro nome é {}'.format(fatiar[0]))
print('Seu último nome é {}'.format(fatiar[len(fatiar) - 1]))

primeiro = (fatiar[0])
numcaracteres = len(primeiro)

print('Seu primeiro nome tem {} letras'.format(numcaracteres))
print('A última letra do seu primeiro nome é {}'.format(primeiro[len(primeiro) - 1]))
