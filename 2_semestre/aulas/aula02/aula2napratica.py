#media minima para ser aprovado
aprovacao=7.0

#media minima para ficar para exame
exame=6.0

#quantidade de bimestres no ano
bimestres=4

#nome do aluno
nome = "Pedro Henrique"


#lista de notas durante o ano - uma por bimestre
notas=[7.8, 8.5, 5.9, 7.1]

#mensagem para ser mostrada ao final da execução
mensagem=''

#instrução de repetição para somar todas as notas do ano
soma=0
for nota in notas:
    soma += nota

#calculo da medía anual
media = soma / bimestres

#instrução de decisão para adicionar texto na variavel "mensagem"
if media>= aprovacao:
    mensagem='Aprovado'
elif media >= exame:
    mensagem = 'Exame'
else:
    mensagem = 'Reprovado'

print("Nome: %s" % nome)
print("Média Anual: %8.2f" % media)
print("Status:%s" % mensagem)