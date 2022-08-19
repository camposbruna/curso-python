'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior_linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if l == 1:
            if matriz[1][c] > maior_linha:
                maior_linha = matriz[1][c]
    print()
    soma_coluna += matriz[l][2]
print('-='*30)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')
print(f'O maior valor da segunda linha é {maior_linha}.')
