#Faça um algoritimo que converta a temperatura de graus celsius para fahrenheit

c = float(input('Informe a temperatuda em ºC: '))
f = c * 9/5 + 32

print('{:.1f}°C = {:.1f}°F'.format(c, f))