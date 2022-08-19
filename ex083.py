'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parenteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem
correta.
'''

expressão = str(input('Digite a expressão: ')).strip()
parent_open = parent_close = 0

for c, v in enumerate(expressão):
    if v == '(':
        parent_open += 1
    elif v == ')':
        parent_close += 1
if parent_open == parent_close:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
