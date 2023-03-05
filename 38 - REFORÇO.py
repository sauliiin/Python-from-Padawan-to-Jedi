nome = str(input('Qual é seu nome?')).strip().title()
print('Muito prazer em te conhecer, {}!' .format(nome))
if nome == 'Gustavo':
    print('Que nome legal você tem!')
else:
    print('Eu prefiro o nome Gustavo, mas... fazer oq neh?!')
print('Olá {}, seja bem vindo!'.format(nome))

# Tudo o que está espaçado pelo TAB, só vai aparecer se a condição fo alcançada. If (se) e else (se não). O que nao tem TAB aparece para todos

n1 = float(input('Digite a nota da sua primeira prova:'))
n2 = float(input('Digite a nota da sua segunda prova:'))
m = (n1 +n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print("Parábens, {}, você foi aprovado!".format(nome))
else:
    print("Que pena {}, você precisa estudar mais.".format(nome))

# Veja que eu não coloquei uma segunda condição m < 6.0. O fato de colocar else já pressupõe isso
# Não precisa fazer com o TAB, apesar de ficar mais bonito e claro, pode fazer simplificado:
print('Parabéns, {}, você foi aprovado!'.format(nome) if m >=6 else 'Que pena {}, você precisa estudar mais.'.format(nome))