'''Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante à função
input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.
ex: n=leiaInt('Digite um n')'''


def leia_int(msg):
    verif = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            verif = True
        else:
            print('{}ERRO! Digite um número inteiro válido{}'.format('\033[31m', '\033[m'))
        if verif:
            break
    return valor


print('-'*30)
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
