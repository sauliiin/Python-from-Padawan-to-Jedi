cont = 1
while cont <= 10:
    print(cont, '...', end='')
    cont += 1
print('Acabou!')

# while true executa a repetição para sempre! break interrompe o loop
s = 0
while True:
    print(cont, '...', end='')
    cont += 1
    if cont == 20:
        break
    s += cont
print(f'Acabou a soma é {s}!')
#f string acimaaaaa!!! Olha como fgacilitou pra colocar o s de soma!

#ATENÇÃO ATENCÃO ONDE VC COLCO A A FUNÇÃO BREAK! SE COLOCAR, POR EX, NO DESAFIO 66, DEPOS DA SOMA, SOMA O 999

nome = 'Jose'
idade = 33
altura = 1.8020374238749
print(f'O {nome} tem {idade} amose {altura:.2f} de altura!')