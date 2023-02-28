frase = str(input('Digite uma frase que possua a letra a: ')).lower().strip()
print('A frase inteira tem {} As e {} palavras'.format(frase.count('a'), len(frase.split())))
separa = frase.split()
print(separa)
print('A primeira palavra é {} e ela tem a? {}'.format(separa[0], 'a' in separa[0]))
print('A última palavra é: {}'.format(separa[len(separa)-1]))
print('A última palavra tem a? {}'.format('a' in separa[len(separa)-1]))

