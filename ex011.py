#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg * alt
tinta = área / 2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m² \n'
      'Para pintar esssa parede, você precisará de {:.2f} litros de tinta.'. format(larg, alt, área, tinta))
