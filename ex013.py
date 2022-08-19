#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioInicial = float(input('Informe o salário do funcionário: R$'))
salarioComAumento = salarioInicial * 1.15

print('O salário do funcionário era de R${:.2f}, com o reajuste de 15% passou a receber R${:.2f}.'.format(salarioInicial, salarioComAumento))