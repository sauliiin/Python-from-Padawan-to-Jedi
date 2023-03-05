n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
print("A soma vale {}.".format(n1+n2))
s = n1+n2
m = n1*n2
d = n1/n2
p = n1**n2
print(f'A soma é {s} e o produto da multiplicação é {m}.', end=" ")
print("A divisão é {:.3f} e a potência é {}.".format(d, p))

print("A soma é {}. \nO produto da multiplicação é {}. \nA divisão é {:.3f}. \nE a potência é {}.".format(s, m, d, p))

"O que é o .3f? Ex: 78/140=0,55714285. Se eu coloco o .3f, vai aparecer só 0,557. "
"E o end? Serve apenas para os dois prints ficarem na mesma linha. Dentro das " " no end, posso colocar o que eu quiser! Teste! "
"Eo \n, faz uma quebra na linha"