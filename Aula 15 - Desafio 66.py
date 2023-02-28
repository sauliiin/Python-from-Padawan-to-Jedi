contador = soma = 0
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Você digitou {contador} números e a soma entre eles é {soma}.')

