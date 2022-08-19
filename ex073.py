'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro
de futebol, na ordem de colocação. Depois mostre:
a) apenas os 5 primeiros colocados;
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time do Avaí.


'''
times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR',
         'Atlético-MG', 'Internacional', 'Flamengo', 'Bragantino',
         'Santos', 'São Paulo', 'Ceará-SC', 'Botafogo', 'Avaí',
         'Goiás', 'Cuiabá', 'Coritiba', 'América-MG', 'Atlético-GO',
         'Fortaleza', 'Juventude')
print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
print('O Avaí está na {}ª posição'.format(times.index('Avaí') + 1))

