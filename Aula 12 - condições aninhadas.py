# if
# elif (else if)
# elif
# elif
# else

# esle é opcional
# se tem só é if é chamado de condição simples. com if e else é condição composta. Se tem if, elif e esle é condicional aninhada

nome = str(input('Qual o seu nome? ')).title().strip()
if nome == 'Saulo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'João':
    print("Seu nome é bem comum no Brasil!")
elif nome in 'Ana Cláudia Jéssica Maria Clara':
    print('Você é tão bonita quanto o seu nome?')
else:
    print('Seu nome não consta no meu banco de dados')
print('Tenha um excelente dia, {}!'.format(nome))

print(nome.split())
print(len(nome.split()))
for c in range (0, len(nome.split())):
    if nome.split()[c] in 'Ana Cláudia Jéssica Maria Clara':
        print(nome.split()[c], end = ', ')
    c += 1
nomebonito = 0
for cont in range (0, len(nome.split())):
    if (nome.split()[cont] in 'Ana Cláudia Jéssica Maria Clara') is True:
        nomebonito += 1
    cont += 1
if nomebonito > 0:
     print('que nome(s) lindo(s)!')