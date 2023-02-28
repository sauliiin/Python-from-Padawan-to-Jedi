dados = {}
dados['Nome'] = str(input('Nome: ')).title().strip()
dados['Nota'] = int(input('Nota: '))
if dados['Nota'] < 6:
    dados['Situação'] = 'Reprovado'
else:
    dados['Situação'] = 'Aprovado'
for key, value in dados.items():
    print(f'{key} é {value}')