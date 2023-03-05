frase = str(input('Digite uma FRASE que possua a letra "a" em alguma ou todas palavras ou em nenhuma: ')).lower().strip()
#Obs: Sacou a diferença entre ' e "? Você pode utilizar os dois a seu favor

print('A frase inteira tem {} As e {} palavras'.format(frase.count('a'), len(frase.split())))
separa = frase.split()
print(separa)
print('A primeira palavra é {} e ela tem a? {}'.format(separa[0], 'a' in separa[0]))
print('A última palavra é: {}'.format(separa[len(separa)-1]))
print('A última palavra tem a? {}'.format('a' in separa[len(separa)-1]))

