temperatura = float(input('informe a Temperatura atual: '))

if temperatura < 7:
    print('Congelando!')
elif temperatura < 10:
    print('Frio!')
elif temperatura < 26:
    print('Otimo!')
else:
    print('Muito Quente!')