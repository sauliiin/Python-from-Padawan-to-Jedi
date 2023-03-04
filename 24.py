nome = str(input('Digite seu nome completo: ')).strip()
#strip() elimina os espaços antes e os espaços depois do nome, se o infeliz assim digitou.
#Dica: o usuário VAI ERRAR! Vc tem que antever isso no seu programa.
print('Seu nome todo em maiúsculo é:', nome.upper())
print('Seu nome todo em minúsculo é:', nome.lower())
print('Seu nome capitalizado é:', nome.title())
print('Seu nome completo contando os espaços tem X caracteres:', len(nome))
print('Seu nome completo sem os espaços tem X caracteres:', len(nome)-nome.count(' '))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))