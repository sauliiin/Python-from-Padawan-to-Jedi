from datetime import date
hoje = date.today().year

dados = dict(Nome=str(input('Qual o seu nome: ')).title().strip(),
             Idade=(hoje - int(input('Em que ano você nasceu? '))),
             CTPS=int(input('Qual o número da sua carteira de trabalho: ')))
if dados['CTPS'] != 0:
    dados['Ano de aposentadoria'] = (int(input('Em que ano começou a trabalhar? ')) + 35)
    dados['Salário'] = float(input('Qual o seu salário? R$ '))
for chave, valor in dados.items():
    print(f'{chave}: {valor}')