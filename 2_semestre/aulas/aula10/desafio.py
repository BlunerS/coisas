opcao = int(input("Bem vindo. Selecione uma opção abaixo: \n 1 - Converter Bitcoin para Real \n 2 - Converter Real para Bitcoin \n 3 - Sair \n" ))


while opcao != 3:
    if opcao:=1:
        bitcoin = float(input("Digite o valor em bitcoin:"))
        print("De acordo com a cotação de 23/08/2022, seus bitcoins valem: R$", bitcoin * 109531.58)
        
    else:
        real = float(input("Digite o valor em real:"))
        print("De acordo com a cotação de 23/08/2022, esse valor em bitcoin resulta em ", real / 109531.58)
else:
    print("O programa irá ser encerrado.")