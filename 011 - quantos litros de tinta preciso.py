print("Cada litro de tinta rende 2m². Quantos litros de tinta eu preciso?")
alt = float(input("Qual a altura da sua parede? "))
larg = float(input("Qual a largura da sua parede? "))
area = alt*larg
print("Sua parede tem {} metros quadrados".format(area))
print("Se cada litro de tinta rende 2m² e sua parede tem {}m², você precisará de {} litros!".format(area, area/2))
