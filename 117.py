notas = {}


def contador(*num, sit=False):
    """
    :param num: Notas registradas.
    :param sit: Mostrar ou não a situação do aluno.
    :return: Analisar as notas do aluno
    """
    print(f'Recebi os valores {num}, que são ao todo {len(num)} números, '
          f'cuja média é {sum(num) / len(num)}, o maior valor é {max(num)} e o menor {min(num)}.')
    notas['Quantidade'] = len(num)
    notas['Maior nota'] = max(num)
    notas['Menor nota'] = min(num)
    notas['Média'] = sum(num)/ len(num)
    if sit is True:
        if sum(num) / len(num) >= 6:
            print('Você foi aprovado!')
        if sum(num) / len(num) < 6:
            print('\033[0;31mVocê foi reprovado!\033[m')


print('Olá! Vamos cadastras as notas das suas avaliações? ')
n1 = int(input(f'Qual a nota da 1ª avaliação? '))
n2 = int(input(f'Qual a nota da 2ª avaliação? '))
n3 = int(input(f'Qual a nota da 3ª avaliação? '))
n4 = int(input(f'Qual a nota da 4ª avaliação? '))
sit = str(input('Quer saber o seu rendimento? (S/N) '))
if sit in 'N' or '':
    contador(n1, n2, n3, n4)
else:
    contador(n1, n2, n3, n4, sit=True)


