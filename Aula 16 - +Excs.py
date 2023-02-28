tupla1 = ('a', 'b', 'c', 'd')
tupla2 = (1, 2, 3, 4)
tupla3 = (2, 4, 5)
tupla4 = tupla1 + tupla2 + tupla3
print(tupla4)

# len significa length (comprimento)
print(len(tupla4))

# quantyas vezes aparece o número 2 na tupla 4?
print(tupla4.count(2))

print(tupla4)
# Em qual posição está o 2? O index pega a primeira ocorrencia do item
print(tupla4.index(2))

tupla = ('Gustavo', 39, 'M', 99.88)
print(tupla)
del(tupla)
