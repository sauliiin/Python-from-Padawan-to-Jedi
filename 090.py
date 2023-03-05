lista = []
pares = []
impares = []
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
print(f'Estes são todos os valores digitados: {lista}.')
pares.sort()
print(f'Os pares são: {pares}.')
impares.sort()
print(f'Os impares são: {impares}.')


#Existe Dev e copiador de código! A diferença entre um e outro é que o copiador de código nunca vai ser um Dev. O Dev está pronto para encarar e resolver desafios! Você pode chegar ao mesmo resultado com códigos diferentes, veja:

núm = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print(f'Estes são todos os valores digitados: {núm}.')
núm[0].sort()
print(f'Os pares são: {núm[0]}.')
núm[1].sort()
print(f'Os impares são: {núm[1]}.')