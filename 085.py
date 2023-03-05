lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = ' '
    while resp not in "SsNn":
        resp = str(input('Desjea continuar (S/N): ')).upper().strip()
    if resp in 'Nn':
        break
print(f'A) A lista possui {len(lista)} valores.')
lista2 = lista[:]
lista2.sort(reverse=True)
print(f'B) A lista em ordem decresente fica assims: {lista2}.')
print('C) O número 5 foi digitado?', end=' ')
if 5 in lista:
    print(f'Sim! Ele está na {lista2.index(5) + 1}ª posição.')
else:
    print('Não.')