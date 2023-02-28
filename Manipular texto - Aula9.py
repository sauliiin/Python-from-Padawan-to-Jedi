# cada caracter ocupa um espaço coçando do zero
print('Manipulando cadeias de texto')

frase = "Curso em Vídeo Phyton"

fatiamento = frase[9]
print(fatiamento)

trecho = frase[9:21]
print(trecho)
trecho2 = frase[9:]
print(trecho2)
trecho3 = frase[:5]
print(trecho3)

frasepulando = frase[9:21:2]
print(frasepulando)
frasepulando2 = frase[9::2]
print(frasepulando2)

numcaracteres = len(frase)
print(numcaracteres)
#muito cuidado com len, veja que no desafio 27, pra ele funcionar em uma fórmula coloquei [], -1

#método compreenssão numero de palvras
fatiar = frase.split()
print(fatiar)
quantaspalavrastemnafrase = len(fatiar)
print(quantaspalavrastemnafrase)

numerodepalavras = len(frase.split())

quantosos = frase.count('o')
print(quantosos)
quantososnumespeaco = frase.count('o', 0, 13)
print(quantososnumespeaco)
print('...')
encontre = frase.find('Vídeo')
print(encontre)
encontrenada = frase.find('SaulinYoda')
print(encontrenada)
print('...')
Existe = 'Curso' in frase
print(Existe)

mudando = frase.replace('Python','Android')
print(mudando)
#errouuuuuuuuu!!!!! Pq alterou, mas nao salvou. Lermbre-se que o sinal = na linguagem de progrmação a gente chama de recebe
frase = "Curso em Vídeo Phyton"
frase3 = frase.replace('Phyton', 'Android')
print(frase3)
#faça um teste:
#frase = "Curso em Vídeo Phyton"
#frase = frase.replace('Phyton', 'Android')
#se eu usar frase ao inves de frase 3, daki pra frente ele vai sempre substituir por android

upper = frase.upper()
print(upper)
#upper é um método, então o () é obrigatório!!!
lower = frase.lower()
print(lower)
capitalize = frase.capitalize()
print(capitalize)
title = frase.title()
print(title)
fatiar = frase.split()
print(fatiar)
juntar = '-'.join(frase)
print(juntar)
contarOs = frase.count('o')
print(contarOs)
contaro = frase.count(('O'))
print(contaro)
print(frase.upper().count('O'))

frase2 = '     Aprenda Phyton   '
print(frase2)
strip = frase2.strip()
print(strip)
stripr = frase2.rstrip()
print(stripr)
stripl = frase2.lstrip()
print(stripl)
#quantos caracteres com e sem os espaços
print(len(frase2))
print(len(frase2.strip()))

#olha olha como faz pra fazer print de texto longo
print("""Persistir na raiva é como apanhar um pedaço de carvão quente com a intenção de o atirar em alguém. 
É sempre quem levanta a pedra que se queima. Um amigo falso e maldoso é mais temível que um animal selvagem; 
o animal pode ferir seu corpo, mas um falso amigo irá ferir sua alma.""")