print('Vamos monstar um triângulo.')
L1 = (float(input('Digite o cumprimento do primeiro lado: ')))
L2 = (float(input('Digite o cumprimento do segundo lado: ')))
L3 = (float(input('Digite o cumprimento do terceiro lado: ')))
if (L1 < L2 + L3) and (L2 < L1 + L3) and (L3 < L1 + L2):
    # Para um triangulo existir, um lado tem que ser menor que a soma dos dois outros lados
    print('Os dados fornecidos possuem dimensões possiveis para construir um triangulo. E', end=" ")
    if (L1 == L2) and (L2 == L3):
# POSE USAR: if L1 == L2 == L3:
        print('o triángulo é equilátero!')
    elif (L1 != L2) and (L2 != L3) and (L1 != L3):
        print('o triángulo é escaleno!')
    elif (L1 != L2) or (L2 != L3) or (L1 != L3):
        print('o triángulo é isóceles!')
else:
    print('Os dados fornecidos NÃO possuem dimensões possiveis para construir um triangulo')
