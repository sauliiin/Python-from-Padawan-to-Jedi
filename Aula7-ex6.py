print("Se você recebe X reais e vai recber um aumento de Y%, qual será seu novo salário?")
X = float(input("Qual o seu salário atual? R$ "))
Y = float(input("Quantos por centos você vai ganhar de aumento? "))
ganho = X*Y/100
novo = X+ganho
print("Seu novo salário será: R$ {:.2f}".format(novo))
