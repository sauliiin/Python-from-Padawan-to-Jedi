# galera = list()
# ouuuu galera = []

galera = [['João', 19], ['Ana', 33], ['Carol', 23], ['Maria', 28]]
print(galera[1])
print(galera[2][1])
for count in galera:
    print(count, end = '')
print('')
for count in galera:
    print(count[0], end=' ')
print('')
for count in galera:
    print(count[1], end=' ')
print('')
for count in galera:
    print(f'{count[0]} tem {count[1]} anos.')

print('=*'*20)

galera2 = list()
dado = list()
for count in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
print(galera2)

for p in galera2:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')
