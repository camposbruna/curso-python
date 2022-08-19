'''
Crie um programa que leia uma frase qualquer
e dia se ela é um palíndromo, desconsiderando
os espaços.
Ex.: Apos a sopa
A sacada da casa
A torre da derrota
O lobo ama o bolo
Anotaram a data da maratona
'''
color = {'reset':'\033[m',
         'yellow':'\033[33m'}

text_original = str(input('Digite a frase: ')).strip().upper()
frase = text_original.split()
frase = ''.join(frase)
frase_invertida = frase[::-1]

print('O inverso de {}{}{} é {}{}{}'.format(color['yellow'], frase, color['reset'], color['yellow'], frase_invertida, color['reset']))

if frase == frase_invertida:
    print('Temos um palíndromo.'.format(color['yellow'], text_original.capitalize(), color['reset']))
else:
    print('A frase digitada NÃO é um palíndromo.'.format(color['yellow'], text_original.capitalize(), color['reset']))

