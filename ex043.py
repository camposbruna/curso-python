'''
Desenvolva uma lógia que leia o peso e a altura de uma pessoa, calcule seu IMC e
mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
cores = {'reset':'\033[m',
         'yellow':'\033[33m',
         'red':'\033[31m',
         'green':'\033[32m',
         'blue':'\033[34m',
         'gray':'\033[1;37m',
         'purple':'\033[35m'}
print('='*40)
print('{}CÁLCULO DE IMC{}'.format(cores['purple'], cores['reset']))
print('='*40)
peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

IMC = peso / (altura ** 2)

if 0 < IMC < 18.5:
    peso_ideal = 18.5 * altura ** 2
    ganhar_kg = peso_ideal - peso
    print('Seu IMC é de {}{:.2f}{} e você está {}ABAIXO DO PESO{}. Você precisa ganhar pelo menos {}{:.2f}kg{}.'. format(cores['blue'], IMC, cores['reset'], cores['blue'], cores['reset'], cores['yellow'], ganhar_kg, cores['reset']))
elif IMC < 25:
    print('Parabéns! Seu IMC é de {}{:.2f}{} e você está no {}PESO IDEAL{}.'. format(cores['blue'],IMC,cores['reset'], cores['blue'], cores['blue']))
elif IMC < 30:
    peso_ideal = 24 * altura ** 2
    perder_kg = peso - peso_ideal
    print('Seu IMC é de {}{:.2f}{} e você está com {}SOBREPESO{}. Você precisa perder {}{:.2f}kg{}.'. format(cores['blue'], IMC, cores['reset'], cores['blue'], cores['reset'], cores['yellow'], perder_kg, cores['reset']))
elif IMC < 40:
    peso_ideal = 24 * altura ** 2
    perder_kg = peso - peso_ideal
    print('Seu IMC é de {}{:.2f}{} e você está {}OBESO{}. Você precisa perder {}{:.2f}kg{}.'.format(cores['blue'], IMC, cores['reset'], cores['blue'], cores['reset'], cores['yellow'], perder_kg, cores['reset']))
elif IMC >= 40:
    peso_ideal = 24 * altura ** 2
    perder_kg = peso - peso_ideal
    print('Seu IMC é de {}{:.2f}{} e você está com {}OBESIDADE MÓRBIDA{}. Você precisa perder {}{:.2f}kg{}.'.format(cores['blue'], IMC, cores['reset'], cores['blue'], cores['reset'], cores['yellow'], perder_kg, cores['reset']))
else:
    print('Digite um valor válido!')
