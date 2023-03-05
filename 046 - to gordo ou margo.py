# IMC = Massa/Altura²
# O IMC ideal fica entre 18,5 e 25
import time

print("----------------------------------")
time.sleep(0.5)
print("        DETECTOR DE PESADÃO       ")
time.sleep(0.5)
print("----------------------------------")
time.sleep(0.5)
nome = str(input('Qual o seu nome? ')).strip().title()
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura**2)
print(f'{nome}, o seu IMC é {imc:.1f} e', end=" ")
if imc < 18.5:
    print('você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('você está com o peso ideal!')
elif 25 <= imc < 30:
    print('você está com sobrepeso!')
elif 30 <= imc < 40:
    print('você está obeso!')
else:
    print('você está com obesidade mórbida!')
