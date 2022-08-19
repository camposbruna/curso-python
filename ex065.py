'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
'''
resposta = 'S'
num = s = c = 0

while resposta == 'S':
    c += 1
    num = int(input('Digite o {}º valor: '.format(c)))
    s += num
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Gostaria de somar outro valor? [S/N] ')).upper().strip()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Valor inválido! Digite novamente se gostaria de continuar [S/N]: ')).upper()
if resposta == 'N':
    print('\n{:=^30}'.format(' RESULTADO '))
    print('Total de números digitados: {}'.format(c))
    print('Média: {:.2f}'.format(s/c))
    print('Maior valor: {}'.format(maior))
    print('Menor valor: {}'.format(menor))




