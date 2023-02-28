dados = {}
pessoal = []
mulheres = []
acima = []
somidade = 0
while True:
    dados['Nome'] = str(input('Qual o nome: ')).title()
    while True:
        dados['Sexo'] = str(input('Qual o sexo? (M/F) ')).upper().strip()[0]
        if dados['Sexo'] in 'MF':
            if dados['Sexo'] == 'F':
                mulheres.append(dados.copy())
            break
        print('ERRO! Digite M ou F!')
    dados['Idade'] = int(input('Qual a idade? '))
    somidade += dados['Idade']
    pessoal.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N!')
    print('-='*15)
    if resp == 'N':
        break
media = somidade / len(pessoal)
for c in range(0, len(pessoal)):
    print(f'{pessoal[c]["Nome"]} tem {pessoal[c]["Idade"]} anos.')
    if pessoal[c]["Idade"] > media:
        acima.append(pessoal[c]["Nome"])
print('-='*15)
print(f'A) Foram cadastradas {len(pessoal)} pessoas.\nB) A média da idade do grupo é {media:.2f}.')
print(f'C) Estas são as mulheres do grupo: ', end='')
for d in range(0, len(mulheres)):
    print(mulheres[d]['Nome'], end=' ')
print()
print(f'D) Estás são as pessoas com idade acima da média {acima}')
print(dados)
print(pessoal)
print(mulheres)
print(acima)

