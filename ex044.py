'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando
o seu preço normal e condição de pagamento:

- À vista: dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' LOJAS GUANABARA '))
preço_normal = float(input('Preço do produto: R$ '))
pagamento = int(input('''FORMAS DE PAGAMENTO
[1] Dinheiro/cheque
[2] Cartão de crédito ou débito: à vista
[3] Cartão de crédito: até 2x
[4] Cartão de crédito: 3x a 12x
Opção selecionada: '''))

if pagamento == 1:
    preço_final = preço_normal * 0.9
elif pagamento == 2:
    preço_final = preço_normal * 0.95
elif pagamento == 3:
    preço_final = preço_normal
    valor_parcela = preço_final / 2
    print('Você irá pagar em 2x de R${:.2f} SEM JUROS'.format(valor_parcela))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? (máx de 12x) '))
    if 3 <= parcelas <= 12:
        preço_final = preço_normal * 1.2
        valor_parcela = preço_final / parcelas
        print('Você irá pagar em {}x de R${:.2f}'.format(parcelas, valor_parcela))
    else:
        print('Número de parcelas inválido!')
        exit()
else:
    print('DIGITE UM VALOR VÁLIDO!')

print('O produto custa R${:.2f} e o preço final será de R${:.2f}'.format(preço_normal, preço_final))

