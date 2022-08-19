'''Crie um programa que tenha uma função chamada fatorial()
que recaba dois parâmetros: o primeiro que indique o número
a calcular e o outro chamado show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial'''


def fatorial(n, show):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-'*30)
print(fatorial(5, show=False))
