somaidades = 0
mulhercommenosde20 = 0
homemmaisveio = 0
for cont in range(1, 5):
    print('{}º nome'.format(cont), '=+=' * 5)
    nome = str(input('Qual o seu nome? ')).strip().title()
    sexo = str(input('Qual o seu sexo? (masc/fem) ')).strip().lower()
    idade = int(input('Qual a sua idade? '))
    # somaidades = somaidades + idade
    somaidades += idade
    if sexo == 'fem' and idade < 20:
        # mulhercommenosde20 = mulhercommenosde20 + 1
        mulhercommenosde20 += 1
    if sexo == 'masc' and idade > homemmaisveio:
        homemmaisveio = idade
        veinho = nome
print('=+=' * 8)
print(
    'A média de idade do grupo é {}.\nO homem mais velho é {}, com {} anos.\nTemos {} mulher(es) com menos de 20 anos.'.format(
        somaidades / 4, veinho, homemmaisveio, mulhercommenosde20))
