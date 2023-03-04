X = int(input("Digite um valor inteiro qualquer: "))
Y = int(input("Digite outro valor inteiro: "))
soma = X + Y
sub = X - Y
mult = X * Y
div = X / Y
pot = X ** Y
print("A soma entre {} e {} é {}.\nA subtração entre {} e {} é {}.\nA multiplicação entre {} e {} é {}.".format(X, Y, soma, X, Y, sub, X, Y, mult))
print("A divisao entre {} e {} é {:.3f}.".format(X, Y, div))
print(f'A divisao entre {X} e {Y} é {div:.3f}.')

# O que é o :.3f? Depois do . (para nós brasileiros, a vírgula) vai mostrar apenas três casas decimais. Ex: 1,644

print("{} elevado a potência de {} é {:.3f}.". format(X, Y, pot))
if (X % 2) == 0:
    print("O número {} você é par".format(X))
else:
    print("O número {} você é impar".format(X))
if (Y % 2) == 0:
    print("O número {} você é par".format(Y))
else:
    print("O número {} você é impar".format(Y))

print('Expressão para achar os número divisíveis por 3: if X % 3 == 0')

