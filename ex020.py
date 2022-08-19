#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
alun1 = (input('Primeiro aluno: '))
alun2 = (input('Segundo aluno: '))
alun3 = (input('Terceiro aluno: '))
alun4 = (input('Quarto aluno: '))
lista = [alun1, alun2, alun3, alun4]
random.shuffle(lista)
print('Ordem de apresentação do trabalho:')
print(lista)
