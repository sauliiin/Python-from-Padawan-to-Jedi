from datetime import date

ano = int(input('Olá jovem padawan, em que ano vc nasceu? '))
anoatual = date.today().year
idade = anoatual-ano
if idade > 18:
    falta = idade-18
    print('Jovem, você já tem {} anos e poderia se alistar no serviço militar a {} ano(s)'.format(idade, falta))
elif idade == 18:
    print('Jovem!!! O que você está fazendo parado, você tem a idade para alistamento militar!')
else:
    falta = 18-idade
    print('Meu jovem padawan, que sorte! Você tem {} anos e falta(m) {} ano(s) para poder se alistar.'.format(idade, falta))
