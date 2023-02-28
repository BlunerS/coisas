nome = ''

altura = 0 #em metros
peso = 0 #em quilos
imc = 0 #resultado imc

def le_dados():
    global nome
    global altura
    global peso

    nome = input('Digite seu nome:')
    altura = float(input('Digite a sua altura(metros): '))
    peso = int(input('Digite seu peso (quilos)'))

def calcula_imc():
    global peso
    global altura

    imc = peso / pow(altura, 2)
    return round(imc, 2)

def avalia_imc():
    imc = calcula_imc()
    if imc < 18.5:
        return 'abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'com peso normal'
    else:
        return 'com sobrepeso'

le_dados()
imc = calcula_imc()
msg = avalia_imc()
print(f'{nome} está {msg}')