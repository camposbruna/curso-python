'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
'''

cidade = (input('Digite o nome da cidade: ')).lower().split()
print('A cidade começa com o nome Santo? {}'.format('santo' in cidade[0]))