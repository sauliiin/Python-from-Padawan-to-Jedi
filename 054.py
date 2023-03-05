import datetime

maiores = 0
anoatual = datetime.date.today().year
print(f"Estamos no ano {anoatual}.")
X = int(input('Vc quer saber a condição de quantos coleguinhas? '))
for cont in range(1, X+1):
    anonasc = int(input(f'Em que ano o {cont}º nasceu: '))
    if anoatual - anonasc >= 18:
        #maiores = maiores + 1
        maiores += 1
        X -= 1
print(f'Dos coleguinhas, {maiores} possuem mais que 18 anos e {X} são de menor.')
