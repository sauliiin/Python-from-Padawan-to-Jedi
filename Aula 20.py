def mostralinha():
    print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')

def mensagem(msg):
    print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
    print(msg)
    print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')

mostralinha()
print(f'{"SISTEMA DE ALUNOS":^30}')
mostralinha()
print()

mensagem(f'{"SISTEMA DE ALUNOS":^30}')
print()

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)
print()

# Dá pra melhorar isso acima neh?
def soma(a, b):
    print(f'{a} + {b} = ', end='')
    s = a + b
    print(s)

soma(4, 5)
soma(8, 9)
soma(2, 1)
# pode fazer assim:  soma = (b=4, a=5)
print()

# Isso abaixo chama empacotamento. * significa desempacotar
def contador(*num):
    print(f'Recebi os valores {num}, que são ao todo {len(num)} números, cuja soma é {sum(num)}.')

contador(2, 1, 7, 8, 9)
contador(1, 2, 3)
print()

def desempacotanome(*nome):
    print(f'Recebi os nomes {nome}, que são todo {len(nome)} nomes.')
desempacotanome('Saulin', 'Olaf', 'Gustaf')
print()

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [2, 3, 4, 8, 34]
dobra(valores)
print(valores)

# A instrução return finaliza a execução e retorna um valor da função.
# return sem qualquer expressão como argumento retorna None.
# Atingir o final da função também retorna None.
