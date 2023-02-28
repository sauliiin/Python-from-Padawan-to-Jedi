import time

from pacotes import texto
from pacotes import funcoes
from pacotes import interface


arq = 'arquivo.txt'
interface.arquivoexiste(arq)
interface.clean(arq)

texto.titulo('MENU PRINCIPAL')
while True:
    resp = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Deletar Pessoa', 'Sair do sistema'])
    if resp == 1:
        interface.lerarquivo(arq)
    elif resp == 2:
        nome = input('\033[1;33mDigite o nome: \033[m').title().strip()
        idade = funcoes.inteiro('\033[1;33mDigite a idade: \033[m')
        time.sleep(0.2)
        interface.cadastrar(arq, nome, idade)
    elif resp == 3:
        deletar = funcoes.inteiro('\033[1;33mQual o número do usuário que deseja descadastrar? \033[m')
        time.sleep(0.2)
        interface.deletalinha(arq, deletar)
    elif resp == 4:
        time.sleep(0.2)
        texto.titulo('Saindo do sistema... Até logo!')
        time.sleep(0.2)
        break
    else:
        time.sleep(0.2)
    texto.linha()