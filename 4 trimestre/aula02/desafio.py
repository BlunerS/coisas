a = float(0)
b = float(0)
c = float(0)

def ler_numeros():
    global a 
    global b 
    global c 

    a = float(input('digite o 1 numero: '))
    b = float(input('digite o 2 numero: '))
    c = float(input('Digite o 3 numero: '))

    print(f'Os numeros lidos são: ', (a),', ', (b), 'e', (c))

ler_numeros()

def calcular_soma():
    global a
    global b
    global c

    soma = float(a+b+c)
    print(f'A soma dos números é:', soma)

calcular_soma()

def calcular_media():
     
     media = (a + b + c / 3)
     print(f'A média desses números é: ',media)

calcular_media()
