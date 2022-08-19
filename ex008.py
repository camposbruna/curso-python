#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

m = float(input('Digite uma distância em metros: '))

print('Quiilomêtro (km): {} \n'
      'Hectômetro (hm): {} \n'
      'Decâmetro (dam): {} \n'
      'Metro (m): {:.2f} \n'
      'Decímetro (dm): {:.2f} \n'
      'Centímetro (cm): {:.2f} \n'
      'Milímetro (mm): {:.2f}'.format((m/1000), (m/100), (m/10), m, (m*10), (m*100), (m*1000)))