from pacotes import texto

while ValueError or TypeError:
    try:
        a = int(input('Digite um número inteiro: '))
    except KeyboardInterrupt:
        texto.atencao('OPERAÇÃO ABORTADA')
        a = b = 0
        break
    except:
        texto.verm('Os dados informados são inválidos! Por favor, digite um número inteiro.')
    else:
        break
    finally:
        print(f'O número inteiro digitado foi {a} e o real {b}.')
while ValueError or TypeError:
    try:
        b = float(input('Digite um número real: '))
    except KeyboardInterrupt:
        texto.atencao('OPERAÇÃO ABORTADA')
        b = 0
        break
    except:
        texto.verm('Os dados informados são inválidos! Por favor, digite um número real.')
    else:
        break
    finally:
        print(f'O número inteiro digitado foi {a} e o real {b}.')

