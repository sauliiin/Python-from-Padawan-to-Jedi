#Tuplas ()
#Listas []
#Dicionários {}
# enumerate é pra tuplas e listas. Pra dicionários é items

# dados = dict() ou dados = {}
dados = {'nome': 'Pedro', 'idade': 23}
print(dados['nome'])
print(dados)
# E pra adicIonar mais dados?
dados['sexo'] = 'M'
del dados['idade']
print(dados.values())
print(dados.keys())
print(dados.items())
for key, value in dados.items():
    print(f'O {key} é {value}')
for k, v in dados.items():
    print(f'O {k} é {v}')

print('*'*20)
print('')

# pode misturar dicionários com listas e tuplas
alunos = [{'nome': 'Saulo', 'idade': 38}, {'nome': 'Olaf', 'idade': 27}, {'nome': 'Gustaf', 'idade': 42}]
print(alunos)
print(alunos[0]['nome'])
c = 0
while c < len(alunos):
    print(f'O {alunos[c]["nome"]} tem {alunos[c]["idade"]} anos')
    c += 1

print('*'*20)
print('')

#pode usar enumerate pq são vários dicionários em uma tupla
for k, v in enumerate(alunos):
    print(f'O {alunos[k]["nome"]} tem {alunos[k]["idade"]} anos')

print('*'*20)
print('')

turma = []
aluno1 = {'nome': 'Saulo', 'idade': 38}
aluno2 = {'nome': 'Olaf', 'idade': 27}
turma.append(aluno1)
turma.append(aluno2)
print(turma)
print(turma[0]['nome'], turma[1]['nome'])
print(aluno1)

print('*'*20)
print('')
colegas = dict()
turma = list()
for c in range(1, 4):
    colegas['nome'] = str(input(f'Digite o nome do {c}º coleguinha: '))
    colegas['idade'] = int(input('Qual a idade do amiguin? '))
    # errado, pra dicionário tem o método próprio abaixo turma.append(colegas[:])
    turma.append(colegas.copy())
print(colegas)
print(turma)
for col in turma:
    for k, v in col.items():
        print(f'O campo {k} tem valor {v}.')