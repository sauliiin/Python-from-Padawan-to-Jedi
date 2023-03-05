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


# Lembrete: Expressão para achar os número divisíveis por 3: if cont % 3 == 0
#Expressão para achar números pares: if cont % 2 == 0
#Expressão para achar números ímpares: if cont % 2 != 0 ou if X % 2 == 1 é impar