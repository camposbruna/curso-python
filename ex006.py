#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))

print('O dobro de {} vale {}. \n'
      'O triplo de {} vale {}. \n'
      'A raiz quadrada de {} vale {:.2f}.'.format(n, (n*2),n, (n*3), n, (n**(1/2))))
