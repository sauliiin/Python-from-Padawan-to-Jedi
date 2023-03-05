# Para criar um programa vc tem que presumir que o usuário vai digitar errado, vai errar, então é necessário orientar o usuário quando ele erra para o programa funcionar sempre bem. 

sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite M ou F! ')).strip().upper()[0]

sexo = 1
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Digite M ou F!')

