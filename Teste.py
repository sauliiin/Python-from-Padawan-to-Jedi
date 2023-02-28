for cont in range(1, 101):
    for i in range(2, cont):
        if cont % i == 0:
            break
    else:
        print(cont, 'é primo')

