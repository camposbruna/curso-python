'''
Crie um programa que leia o nome completo de uma pressoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras ao total (sem considerar espaços);
- Quantas letras tem o primeiro nome.
'''

nome = (input('Informe o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))

nome = nome.split()
print('Seu nome tem ao todo {} letras.'.format(len(''.join(nome))))
print('Seu primeiro nome tem {} letras'.format(len(nome[0])))
