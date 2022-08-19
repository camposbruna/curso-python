'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
Depois disso, você deve mostrar para cada palavra, quais são suas vogais.
'''

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
                 'Curso', 'Gratis', 'Estudar', 'Praticar',
                 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')