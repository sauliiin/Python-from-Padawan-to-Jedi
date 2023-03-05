print("Se o produto custa X reais e na promoção vai ter Y% de desconto, qual o valor Z final?")
X = float(input("Qual o preço atual do produto? R$ "))
Y = float(input("Qual a porcentagem do desconto? "))
desc = X*Y/100
preço = X-desc
print("Durante a promoção, o produto custará: R$ {:.2f}.".format(preço))


