from time import sleep


def maior(*num):
    print('Analisando os valores...')
    sleep(1)
    print(f'Recebi os valores {num}, que ao todo são {len(num)} números. \nO maior valor é {max(num)}.')
    print('-=' * 20)


maior(2, 1, 7, 8, 9)
maior(1, 2, 3)
