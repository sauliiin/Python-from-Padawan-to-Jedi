nome = str(input('Qual é seu nome?')).strip().title()
print('Muito prazer em te conhecer, {}!' .format(nome))
if nome == 'Gustavo':
    print('Que nome legal você tem!')
else:
    print('Eu prefiro o nome Gustavo, mas...')
    fatiar = nome.split()
    primeiro = (fatiar[0])
    numcaracteres = len(primeiro)
    ultimaletra = primeiro[len(primeiro) - 1]
    if ultimaletra == 'a':
        print('Olá {}, seja bem vinda!'.format(nome))
    else:
        print('Olá {}, seja bem vindo(a)!'.format(nome))


