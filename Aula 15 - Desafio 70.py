from pacotes import funcoes
soma = menor = maior = cont1 = cont2 = 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Informe preço: R$ '))
    soma += preco
    cont1 += 1
    if menor == 0 or preco < menor:
        barato = nome
        menor = preco
    if preco > maior:
        caro = nome
        maior = preco
    if preco > 1000:
        cont2 += 1
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Deseja continuar? S/N: ')).upper().strip()[0]
    if perg == 'N':
        break
print(f'Total gasto: R$ {soma} em {cont1} produtos. {cont2} produto(s) custou mais de mil reais.\nO produto mais barato foi o {barato}, que custou R$ {menor:.2f}. O mais caro foi o {caro}, custando R$ {maior:.2f}.')
print('{:-^40}'.format('FIM DOPROGRAMA'))
