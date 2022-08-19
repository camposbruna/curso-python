#um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
alun1 = (input('Digite o nome do primeiro aluno: '))
alun2 = (input('Digite o nome do segundo aluno: '))
alun3 = (input('Digite o nome do terceiro aluno: '))
alun4 = (input('Digite o nome do quarto aluno: '))
lista = [alun1, alun2, alun3, alun4]

alunSort = random.choice(lista)

print('Aluno escolhido: {}'.format(alunSort))