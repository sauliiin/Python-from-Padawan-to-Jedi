# Try, vc tenta uma operação. Se falhar, except (Obs: pode ter mais de um except). Se não der problema em nenhum dos dois, else.
# Se vc quiser alguma coisa independente dos resultados anteriores., usa finally.
# Finally e else são opcionais.
# para identificar o erro na tela, vc pode escrever: except Exception as x

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
#except Exception as x:
#    print(f'O erro identificadoi foi {x.__class__}')
except (ValueError, TypeError):
    print('Os dados informados não são válidos')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('OPERAÇÃO ABORTADA')
except:
    print('ERRO! Ou vc digitou zero ou uma string!')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre!')
