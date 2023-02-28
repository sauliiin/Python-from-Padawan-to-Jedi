# help() ou, por ex help(print)
# excuta o help() e olha do lado! Vc pode digitar no terminal qualquer coisa do phyton que ele te passa
# o manual. Digita, por exemplo: print ou datetime. O help vai te esnisnar sobre print. Pra sair: quit

def contador(inicio, fim, passo):
    """
    Faz uma contagem do início ao fim pulando passos
    :param inicio: inicio da contagem
    :param fim: fim da contagem
    :param passo: pulos ao contar
    :return: sem retorno
    """
    contador = inicio
    while contador <= fim:
        print(f'{contador}', end='..')
        contador += passo
    print('FIM!')

contador(2, 10, 2)

#hummmm... E se alguem ou vc for usar o codigo de alguem, como compreender?
#para isso, em codigos complexos, é importante fazer docstring. Basta abaixo do código que vc quer explicar utilizar 3 aspas: """     """
#Dai, quando digital help(contador), vai aparecer explicado o contador.

help(contador)

#PARAMETRO OPCIONAL! Não digitei c e d mesmo assim deu pra somar só 2 numeros
print()

def soma(a, b, c=0, d=0):
    soma = a + b + c + d
    print(f'O resultado da soma é {soma}')

soma(1, 3, 4, 7)
soma(5, 3, 2)
soma(a=4, b=5)

print()
#ESCOPO DE VARIÁVEIS!
def teste(x, n):
    x = 8
    print(f'O valor de X é {x} e n é {n}')
n=2
print(f'O valor de n é {n}')
#print(f'O valor de x é {x}')

# Como x foi definido só na função, ele não vai paparecer no programa principal como uma vairável
# É oq a gente chama de variável global (n) e vairável local (x).
#Haaaaaaa, mas se eu quiser que a função mude o valor!:
print()
def teste2(b):
    global a
    # quando eu escrevo global, eu nao estou transformando a variavel abaixo em global, mas sim fazendo com que a variavel 'a'
    #global, do proprama principal, seja trazida para dentro do def. Neste caso abaixo, eu fiz o a principal receber o 8 e virar 8
    a = 8
    print(f'O valor de A é {a}')
a = 2
(teste2(a))
print(f'O valor de a é {a}')

#RETORNO DE VALORES
def soma2(a=0, b=0, c=0, d=0):
    s = a + b + c + d
    return s
# A instrução return finaliza a execução e retorna um valor da função.
# return sem qualquer expressão como argumento retorna None.
# Atingir o final da função também retorna None.
r1 = soma2(1, 3, 4, 7)
r2 = soma2(5, 3)
print(f'Meu calculos foram {r1} e {r2}.')
print()

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par.')
else:
    print('É impar')


