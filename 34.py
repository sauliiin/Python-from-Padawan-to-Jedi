#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
import time

salario = float(input('Digite o seu salário atual:'))
print('\033[1;31;40m**CALCULANDO**\033[m'*3)
time.sleep(3)
if salario <= 1250:
    print('Seu salário reajustado será \033[7;31;40mR$ {:.2f}\033[m'.format(salario*1.15))
else:
    print('Seu salário reajustado será \033[7;31;40mR$ {:.2f}\033[m'.format(salario*1.1))

#prof
if salario <= 1250:
    novo = (salario*1.15)
else:
    novo = (salario*1.10)
print('Seu salário reajustado será R$ {:.2f}'.format(novo))

