from pacotes import funcoes

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Não vale número repetido')
    resp = ' '
    while resp not in "SsNn":
        resp = funcoes.simnao('Desjea continuar (S/N): ')
    if resp in 'Nn':
        break
print(lista)
lista.sort()
print(f'A lista em ordem crescente é: {lista} .')


