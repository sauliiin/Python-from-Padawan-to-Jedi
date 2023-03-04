print(" Oi "*5)
nome = input("Qual é seu nome? ").title()
print(f'Prazer em te conhecer {nome:20}!')
print("Prazer em te conhecer {:>20}!".format(nome))
print(f'Prazer em te conhecer {nome:<20}!')
print("Prazer em te conhecer {:^20}!".format(nome))
print("Prazer em te conhecer {:-<20}!".format(nome))
print('Prazer em te conhecer {:*^20}!'.format(nome))
informal = nome.strip().title().split()[0]
print(f'E aeeeee {informal}, bele?')

# O {:20} indica que este campo tera 20 espaços. O > alinha à direita, o < à esquerda e o ^ centraliza. 