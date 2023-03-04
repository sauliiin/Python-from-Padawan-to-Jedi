n = input("Digite qualquer coisa: ")
print("Está coisa é um número?", n.isnumeric())
print("Está coisa é alfabética?", n.isalpha())
print("Está em maíusculo?", n.isupper())
print("Está em mínusculo?", n.islower())
print("Está coisa começa com maiusuculo?", n.istitle())
print("O tipo primitico desse valor é", type(n))

# isnumeric ou isidentifier é uma pergunta. É um número, resposta true ou false.
# o n, nas formulas acima é um "objeto" (string).