soma = 0
#X % 2 = 1
for cont in range(0, 500):
    n = 3*cont
    # Expressao para achar os número divisiveis por 3: if cont % 3 == 0
    if n % 2 == 1 and n < 500:
        print(n)
        #soma = soma + n
        soma += n
print(soma)