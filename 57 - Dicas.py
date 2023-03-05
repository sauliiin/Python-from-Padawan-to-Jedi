cont = maiores = masc = muies = 0
# IMPORTAMTEEEE!! EU DECLAREI A IDADE ANTES DA PERGUNTA, PORQUE A CADA PERGUNTA O VALOR TEM QUE RETORNAR PARA -1
# SE NAO, NÃO PERGUTA DE NOVO. O MESMO VALE PARA O SEXO E OPCAO, SÓ QUE COMO ELES SAO STRINGS, NAO POSSO DECLARAR UM
# NUMERO, TEM QUE SER UM ESPAÇO ' '. e TEM QUE SER DENTRO PQ PERGUNTA A CADA RODADA
while True:
    cont += 1
    idade = -1
    while idade < 0 or idade > 130:
        idade = int(input(f'Quantos anos tem o {cont}º candidato? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? (Masc/Fem) ')).upper().strip()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade > 20:
        muies += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continar ? (S/N) ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Dos cadidatos, {maiores} tem mais que 18 anos, {masc} são homens e {muies} são mulheres com mais de 20.')