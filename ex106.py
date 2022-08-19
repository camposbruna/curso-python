'''Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM' o programa será encerrado.
OBS: use cores.'''

from time import sleep
cores = {
    'limpa': '\033[m',
    'azul': '\033[44m',
    'verde': '\033[42m',
    'branco': '\033[7m',
    'vermelho': '\033[1;41m'
}


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 'azul')
    print(f'{cores["branco"]}', end='')
    help(com)
    print(f'{cores["limpa"]}', end='')
    sleep(1)


def título(msg, color):
    comp = len(msg) + 4
    print(f'{cores[color]}{"~" * comp}')
    print(f'  {msg}')
    print(f'{"~" * comp}\n{cores["limpa"]}', end='')
    sleep(1)


while True:
    título('SISTEMA DE comando PyHELP', 'verde')
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando in 'fim':
        título('ATÉ LOGO!', 'vermelho')
        break
    ajuda(comando)




