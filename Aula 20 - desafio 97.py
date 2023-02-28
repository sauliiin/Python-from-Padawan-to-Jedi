def ajustalinha(n):
    print('~'*len(n))
    print(n)
    print('~'*len(n))


while True:
    n = str(input('Digite uma palavra ou frase: '))
    ajustalinha(n)
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N!')
    if resp == 'N':
        break

        
