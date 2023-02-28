#Um professor quer escolher a ordem de apresentação dos seus quatro alunos
import random as rd

print('Gabriel, Olavo, Livia e Cintia. Quem apresentará primeiro, segundo, terceiro e por último?')
n1 = 'Gabriel'
n2 = 'Olavo'
n3 = 'Livia'
n4 = 'Cintia'
lista = [n1, n2, n3, n4]
rd.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)




