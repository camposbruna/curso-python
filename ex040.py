'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
cores = {'reset':'\033[m',
         'yellow':'\033[33m',
         'red':'\033[31m',
         'green':'\033[32m',
         'gray':'\033[1;37m',
         'purple':'\033[35m'}

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2)/2
situação = ''
if 5 > média >= 0:
    situação = 'REPROVADO'
elif 7 > média >= 5:
    situação = 'EM RECUPERAÇÃO'
elif 10 >= média >= 7:
    situação = 'APROVADO'
else:
    print('{}Digite um valor válido!{}'.format(cores['red'], cores['reset']))


print('Você obteve média {}{:.1f}{} e está {}{}{}'.format(cores['purple'], média, cores['reset'], cores['purple'], situação, cores['reset']))