# palídramo:
# APOSASOPA de tras pra frente é APOSASOPA
# o lobo ama o bolo
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print(frase)
numcaracteres = len(frase)
frasedetras = frase[numcaracteres::-1]
print(frasedetras)
if frasedetras == frase:
    print('Você digitou um pálidramo')

print("=+"*5)
print("Agora com um código diferente e desconsiderando espaços!")
print(frase)
numcaracteres = len(frase)
n1, n2 = '', ''
for cont in range(0, numcaracteres):
    if frase[0 + cont] != " ":
        n1 = n1 + (frase[0 + cont])
print(n1)
for cont in range(numcaracteres, 0, -1):
    if frase[cont - 1] != " ":
        n2 = n2 + (frase[cont - 1])
print(n2)
if n1 == n2:
    print('Você digitou um pálidramo')