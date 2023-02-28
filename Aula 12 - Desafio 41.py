from datetime import date

ano = int(input('Olá jovem padawan, em que ano vc nasceu? '))
anoatual = date.today().year
idade = anoatual-ano
if idade < 9:
    print('Jovem, você tem {} anos e está na categoria MIRIM!'.format(idade))
elif 9 <= idade < 14:
    print('Jovem, você tem {} anos e está na categoria INFANTIL!'.format(idade))
elif 14 <= idade < 19:
    print('Jovem, você tem {} anos e está na categoria JÚNIOR!'.format(idade))
elif 19 <= idade < 20:
    print('Jovem, você tem {} anos e está na categoria SÊNIOR!'.format(idade))
else:
    print('Jovem, você tem {} anos e está na categoria MASTER!'.format(idade))
