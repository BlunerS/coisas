nomePaciente = input("Digite o nome do paciente ")
telefonePaciente = input("Digite o telefone do paciente ")
peso = float(input("Digite o peso do paciente "))
altura = float(input("Digite a altura do paciente "))

def imc(peso, altura):
    resultado=peso / (altura*altura)
    return resultado

print("O imc do paciente ",nomePaciente," é", imc(peso, altura))