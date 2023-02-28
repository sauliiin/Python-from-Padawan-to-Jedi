#escreva um programa para aprovar emprestimo de financiamento de casa
#programa vai ler valor da casa, salario, quantos anos vai financiar
#prestação nao pode ser superior a 30% do salário
import time

nome = (str(input('Seja muito bem vindo! Qual o seu nome? ')))
casa = (float(input(f'Olá {nome}, qual o valor do imóvel que você quer financiar? R$ ')))
ano = (int(input('Em quantos anos você quer finaciar o imóvel? ')))
salario = (float(input('Por último, me informe, por favor, qual o seu salário atual: R$ ')))
print(3*'**PROCESSANDO**')
time.sleep(1)
parcela = casa / (ano * 12)
if parcela > salario*0.3:
    print('Sinto muito {}, mas o valor das parcelas nessas condições excede 30% do seu salário e não é autorizado o financiamento.'.format(nome))
else:
    print('Que ótimo {}, seu financiamento foi aprovado e o valor mensal da sua parcela será de R${:.2f}!'.format(nome, parcela))
