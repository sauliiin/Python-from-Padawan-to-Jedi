temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continua? (S/N) ')).strip()
    if resp in 'Nn':
        break
print('O(s) mais pesado(s): ', end='')
for p in princ:
    if p[1] == mai:
        print(p[0])
print('O(s) menos pesado(s): ', end='')
for p in princ:
    if p[1] == men:
        print(p[0])
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi {mai} e o menor {men}.')
