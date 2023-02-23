nota = int(input('Digite uma nota: '))

if nota > 40:
    print('Reprovado')
    print('Estude Mais')
else:
    if nota < 60:
        print('Recuperação')
        print('Você consegue')
    else:
        print('Aprovado')
        print('Parabéns')