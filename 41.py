from datetime import date

ano = int(input('Olá jovem Padawan, em que ano vc nasceu? '))
anoatual = date.today().year
idade = anoatual-ano
if idade > 18:
    falta = idade-18
    print(f'Jovem, você já tem {idade} anos e poderia se alistar no serviço militar a {falta} ano(s)')
elif idade == 18:
    print('Jovem!!! O que você está fazendo parado, você tem a idade para alistamento militar!')
else:
    falta = 18-idade
    print('Meu jovem Padawan, que sorte! Você tem {idade} anos e falta(m) {falta} ano(s) para poder se alistar.')
