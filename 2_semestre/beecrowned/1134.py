alcool=0
gasolina=0
diesel=0
fim=0

while fim != 4:
    fim=int(input())
    if fim == 1:
        alcool = alcool + 1
    if fim == 2:
        gasolina = gasolina + 1
    if fim == 3: 
        diesel = diesel + 1
print('Muito Obrigado!')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel {}'.format(diesel))