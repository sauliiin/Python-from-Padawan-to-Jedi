#listas ao contrário de tuplas, não são imutáveis.
#pode inclusive adicionart mais itens - lista.append('bicileta')
#pode inserir em qualquer lugar na posiçãpo da lista - lista.insert(0, 'bicicleta')
#parta apagar elementos: dellista[3] ou lista.pop[3] ou lista.remove['bicicleta']
import random

lista = [1, 4, 5, 6]
print(lista)
lista[0] = 12
print(lista)
lista.append(8)
print(lista)
lista.insert(0, 7)
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(f'Essa lista tem {len(lista)} elementos.')

lista2 = [random.randint(0, 20), random.randint(0, 20)]
print(lista2)
lista2 = list(range(0, 10))
print(lista2)
lista2 = list(range(10, 0, -1))
print(lista2)

lista3 = ['pizza', 'biscoito', 'revista', 'pizza', 'bicicleta']
lista3.remove('pizza')
print(lista3)
for posicao, valor in enumerate(lista3):
    print(f'Na posição {posicao} está o item {valor}')

lista4 = [2, 3, 4, 7]
print(lista4)
b = lista4
b[2] = 18
print(lista4)
print(b)

lista4 = [2, 3, 4, 7]
b = lista4[:]
b[2] = 18
print(lista4)
print(b)