import math

maiorpeso = menorpeso = 0
galera = list()
dados = list()
gordos = list()
magros = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    if dados[1] > maiorpeso:
        maiorpeso = dados[1]
    elif menorpeso == 0 or dados[1] < menorpeso:
        menorpeso = dados[1]
    dados.clear()
    resp = str(input('Deseja continua? (S/N) ')).strip()
    if resp in 'Nn':
        break
for count in galera:
    if count[1] >= 100:
        gordo = count[0]
        gordos.append(gordo)
    elif count[1] <= 70:
        magro = count[0]
        magros.append(magro)
print(f'Foram cadastradas {len(galera)} pessoas, sendo: \nO(s) mais pesado(s) {gordos} e o(s) mais magro(s) {magros}')
print(f'O maior peso registrado foi {maiorpeso} e o menor {menorpeso}')

