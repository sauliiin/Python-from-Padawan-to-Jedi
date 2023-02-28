nome = str(input('Digite o nome de uma cidade: ')).title().strip()
print('Será que a Cidade COMEÇA ou não com a palavra Santo?')
existe = 'Santo' in nome[:5]
if ('Santo' in nome[:5]) is True:
    # Santo tem 5 letras
    print(f'A cidade {nome} começa com a palavra Santo.')
elif ('Santo' in nome) is True:
    # sem o parenteses não funciona direito
    print(f'A cidade {nome} não começa mas possui a palavra Santo.')
else:
    print('A cidade digitada não possui a palavra Santo.')
print(existe)

