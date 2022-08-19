'''
Faça um programa que jogue par ou ímpar com o computador. O jogo sé será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas ele conquistou no final do jogo.
'''

from random import randint
s = v = 0

print('=-'*20)
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-'*20)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opção = ' '

    while opção not in 'PI':
        opção = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if opção == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    if opção == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-' * 40)
print(f'GAME OVER! Você venceu {v} vezes')
