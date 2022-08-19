'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aárece a primeira vez;
- Em que posição ela aparece a última vez.
'''

txt = str(input('Digite uma frase: ')).lower().strip()

print('A letra A aparece {} vezes na frase.'.format(txt.count('a')))
print('A primeira letra A apareceu na posição {}.'.format(txt.find('a')+1))
print('A última letra A apareceu na posição {}.'.format(txt.rfind('a')+1))