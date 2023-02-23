largura_g = float(input('Insira a Largura da Garagem: '))
profundidade_g = float(input('Insira a Profundidade da Garagem: '))
#Calculo area da Garagem
area_g = largura_g * profundidade_g

largura_t = float(input('Insira a Largura do Terreno: '))
profundidade_t = float(input('Insira a Profundidade do Terreno: '))
#Calculo area do terreno
area_t = largura_t * profundidade_t

#Caclulo porcentagem de ocupação da garragem dentro do terreno
ocupacao = (area_g/area_t) * 100
print('A garagem ocupa um total de:', ocupacao, '% de todo terreno')