lista = []
lista2 = []
lista3 = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista2.append(n)
    else:
        lista3.append(n)
    resp = ' '
    while resp not in "SsNn":
        resp = str(input('Desjea continuar (S/N): ')).upper().strip()
    if resp in 'Nn':
        break
print(f'Considerando todos os núimeros digitados, esta é a lista: {lista}.')
print(f'Esta é a lista dos números pares: {lista2}.')
print(f'Esta é a lista dos números ímpares: {lista3}.')