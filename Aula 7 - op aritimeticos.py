X = int(input("Digite um valor qualquer: "))
Y = int(input("Digite outro valor: "))
soma = X + Y
sub = X - Y
mult = X * Y
div = X / Y
pot = X ** Y
print("A soma entre {} e {} é {}.\nA subtração entre {} e {} é {}.\nA multiplicação entre {} e {} é {}.".format(X, Y, soma, X, Y, sub, X, Y, mult))
print("A divisao entre {} e {} é {:.3f}.".format(X, Y, div))
print("{} elevado a potência de {} é {.3f}.". format(X, Y, pot))
if (X % 2) == 0:
    print("O número {} você é par".format(X))
else:
    print("O número {} você é impar".format(X))
if (Y % 2) == 0:
    print("O número {} você é par".format(Y))
else:
    print("O número {} você é impar".format(Y))

print('Expressao para achar os número divisiveis por 3: if X % 3 == 0')

# + é adição
# - é subtração
# * é multiplicação
# / é divisão
# ** é potencia. Ex 5²=25
# // é divisão inteira. Ex: 5/2=2,5. A divisão inteira é o valor inteiro, ou seja, 2. Então, 5//2=2
# Sempre que X%2=0, o número é PAR. Se X%2=1 é impar
# % é o resto da divisão inteira. Se 5//2==2, se a gente soma 2 com 2, quanto sobra (resto)? 1
# == é igual!

#Ordem de precedência (quais operadores são executados em primeiro em uma expressão aritimética:
#1º - ()
#2º - **
#3º - *,/,//,%
#4º - +,-

#5+3*2==11 Observando a ordem de precedencia: 3*2=6 ; 5+6=11
#3*5+4**2==31 Observando a ordem: 4**2 (4²=16) ; 3*5=15 ; então 15+16=31
#3*(5+4)**2== Pela ordem: 5+4=9 ; 9²=81 ; 3*81=243