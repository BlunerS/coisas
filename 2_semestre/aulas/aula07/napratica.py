nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))


if idade>=18:
    print('Maior de idade')
else:
    print('Menor de idade')
    print('Não é permitida sua inscrição')

sexo=str(input('Digite(F) - Feminino, (M) - Masculino: ').upper())

if sexo=='M':
    print('Sexo Masculino.')
    print('Numero CAM: ')
elif sexo =='F':
    print('Sexo Feminino.')
else:
    print('Sexo Inválido')