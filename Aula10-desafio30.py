# número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import time
import math
numero = int(input('Digite um número inteiro: '))
par = math.trunc(numero / 2)
print('\33[1;31;46m...PROCESSANDO...\033[m' * 5)
time.sleep(1)
if numero / par == 2.0:
    print('\33[1;32mO numero é PAR!\033[m')
else:
    print('\33[4;33mO número é IMPAR!\033[m')
