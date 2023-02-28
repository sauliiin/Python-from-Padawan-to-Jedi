import time

nome = (str(input('Digite o seu nome: '))).strip().title()
n1 = (float(input('Qual a sua nota na primeira prova? ')))
n2 = (float(input('E na segunda? ')))
media = (n1+n2)/2
print(f'{nome}, a sua nota média foi {media:.2f}. Deixe-me consultar no sistema a sua situação.')
print('=+=Processando=+='*3)
time.sleep(2)
if media <= 5.0:
    print('REPROVADO!')
elif 5.0 < media <= 5.9:
    print('Você está de recuperação, FORÇA!')
else:
    print('Parábens, você foi aprovado e está de férias!')