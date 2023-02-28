import time

from pacotes import texto
from pacotes import funcoes

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
# rt é read text
    except FileNotFoundError:
        a = open(nome, 'wt+')
#wt+ é write text e o + cria se nao existe

def menu(lista):
    c = 1
    for item in lista:
        texto.azul(f'{c} - {item}')
        c += 1
        time.sleep(0.3)
    texto.linha()
    opc = funcoes.inteiro('Opção: ')
    return opc


def cadastrar(arq, nom='desconhecido', i=0):
    try:
        a = open(arq, 'at')
        # a de append, t de texto, e, se quiser criar arquivo, at+
        a.write(f'{"->"};{nom};{i}\n')
        print(f'Novo registro em nome de {nom} concluído com sucesso.')
    except:
        print('\033[1;30;41mERRO!\033[m')
    finally:
        a.close()

def lerarquivo(nome):
    cont = 0
    try:
        a = open(nome, 'rt')
        # Asssim le tudo sem formaatr! print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            cont += 1
            dado[0] = cont
            time.sleep(0.2)
            print(f'{dado[0]:<2}{dado[1]:<18}{dado[2]:^4}anos')
        a.close()
    except:
        texto.atencao('Erro!!!')


def line_count(nome):
    with open(nome) as f:
        cont = 0
        for line in f:
            cont += 1
    return cont


def deletalinha(nome, linha):
    # esta função conta linhas
    with open(nome) as f:
        cont = 0
        for line in f:
            cont += 1
    #return cont
    if linha <= cont:
        with open(nome, 'r') as f:
            # reading line by line
            lines = f.readlines()
            # pointer for position
            ptr = 1
            # opening in writing mode
            with open(nome, 'w') as fw:
                for line in lines:
                    if ptr != linha:
                        fw.write(line)
                    ptr += 1
        print("\033[1;31mExclusão concluída com sucesso.\033[m")
    else:
        print('\033[1;30;41mERRO! Verifique se digitou um número válido.\033[m')

def clean(nome):
#limpa espaços vazios e linhas com erro caso existam
    for a in range (0,  line_count(nome)):
        cont = 0
        try:
            a = open(nome, 'rt')
            for linha in a:
                dado = linha.split(';')
                try:
                    dado[2] = dado[2].replace('\n', '')
                    cont += 1
                except IndexError:
                    with open(nome, 'r') as f:
                        lines = f.readlines()
                        ptr = 1
                        with open(nome, 'w') as fw:
                            for line in lines:
                                if ptr != (cont + 1):
                                    fw.write(line)
                                ptr += 1
        finally:
            a.close()

def cleann(nome):
#limpa espaços vazios e linhas com erro caso existam
    for a in range (0,  line_count(nome)):
        a = open(nome, 'rt')
        cont = 0
        try:
            for linha in a:
                dado = linha.split(';')
                try:
                    dado[2] = dado[2].replace('\n', '')
                    cont += 1
                except IndexError:
                        lines = a.readlines()
                        ptr = 1
                        with open(nome, 'w') as fw:
                            for line in lines:
                                if ptr != (cont + 1):
                                    fw.write(line)
                                ptr += 1
        finally:
            a.close()


