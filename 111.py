import pacotes.funcoes


def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade < 16:
        return f'Com {idade} anos, ainda não pode votar!'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos, O voto é opcional! '
    elif 18 <= idade < 70:
        return f'Com {idade}, você é "obrigado" a votar.'


while True:
    resp = int(input('Em que ano você nasceu? '))
    print(voto(resp))
    resp1 = pacotes.funcoes.simnao('Deseja continuar? (S/N) ')
    if resp1 == 'N':
        break
