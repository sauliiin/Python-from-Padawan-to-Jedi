turma=[]
a = {'nome': 'Olaf', 'idade': 12}
b = {'nome': 'Gustaf', 'idade': 14}
c = {'nome': 'Saulin', 'idade': 7}


turma.append(a)
turma.append(b)
turma.append(c)
print(turma)
# enumerate é para tuplas e listas!
for posicao, valor in enumerate(turma):
    print(f'Para a posição {posicao} tem o valor {valor}.')

print('*'*20)

# turma tem 3 valores, cont é 0 a 2
for cont in turma:
    for chave, valor1 in cont.items():
        print(f'O campo {chave} tem valor {valor1}.')

print('*'*20)

#na posição 0 da turma, temos os campos {'nome': 'Olaf', 'idade': 12}, para obter o valor do nome, é só [0]["nome"]
for posic, value in enumerate(turma):
    print(f'O {turma[posic]["nome"]} tem {turma[posic]["idade"]} anos')

print('*'*20)
dicionario = {'nome': 'Olaf', 'idade': 12, 'nome': 'Gustaf', 'idade': 14, 'nome': 'Saulin', 'idade': 7}
for key, value in dicionario.items():
    print(f'O {key} é {value}')
# Por que deu errado? Poruqe dicionário é para armazenar vários dados de um mesma pessoa, ou produto. Dai eles trabalham melhor com tuplas,
#porque você consegue farmazernar dados de varias pessoas ou produtos.