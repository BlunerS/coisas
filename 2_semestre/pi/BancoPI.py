from re import X
import xlsxwriter
import pandas as pd
import pandas

# verificar se arquivo existe
try:
    with open('banco.xlsx', 'r') as f:
        x = 0
except IOError:
    # criar o arquivo excel
    workbook = xlsxwriter.Workbook('C:/a/faculdade/2_semestre/Python/Atividades_faculdade/pi/banco.xlsx')

    # adicionar planilhas dentro do arquivo com seus respectivos nomes
    worksheet1 = workbook.add_worksheet('DOADOR')
    worksheet2 = workbook.add_worksheet('RECEPTOR')
    worksheet3 = workbook.add_worksheet('FILIAL')
    worksheet4 = workbook.add_worksheet('ESTOQUE')
    worksheet5 = workbook.add_worksheet('DOACOES')

    # adicionra colunas padrões dentro das planilhas

    # planilha doador
    worksheet1.write(0, 0, 'CODIGO')
    worksheet1.write(0, 1, 'NOME')
    worksheet1.write(0, 2, 'CPF')

    # planilha receptor
    worksheet2.write(0, 0, 'CODIGO')
    worksheet2.write(0, 1, 'NOME')
    worksheet2.write(0, 2, 'CPF')

    # planilha filial

    worksheet3.write(0, 0, 'QUANTIDADE')
    worksheet3.write(0, 1, 'ROUPAS')

    # planilha estoque

    worksheet4.write(0, 0, 'CODIGO')
    worksheet4.write(0, 1, 'PRODUTO')
    worksheet4.write(0, 2, 'COD_FILIAL')
    worksheet4.write(0, 3, 'SITUACAO')  # se está disponivel ou não

    # planilha doacoes

    worksheet5.write(0, 0, 'COD_DOADOR')
    worksheet5.write(0, 1, 'COD_FILIAL')
    worksheet5.write(0, 2, 'COD_PRODUTO')
    worksheet5.write(0, 3, 'COD_DOACAO')



nomes = ['A']  # QUANDO TIVER O BANCO, irei substituir isso
countcolunas = 1



def cadastroDoador():
    found = False
    for i in range(len(nomes)):
        if nomes[i] == nome:  # USUARIO CADASTRADO
            print(nomes[i])
            found = True
    if found == False:
        print(nome)
        print("Registrado ", nome, cpfs + "!")

Endereço1 = 'Rua Capitão Cruz, 1474, Centro, Montenegro'

while True:
    title = 'Seja bem vindo(a) a plataforma do Amigo Fritz!'
    print('--' * 25)
    print(title.center(50))
    print('--' * 25)
    nome = input('Por favor informe seu nome de usuário: ').strip()
    while nome.isnumeric():
        nome = input('Valores incorretos.\nPor favor informe seu nome de usuário: ').strip()
    cpfs = input('Por favor informe seu CPF: ').strip()
    cadastroDoador()
    while not cpfs.isnumeric():
        cpfs = input('Valores incorretos.\nPor favor informe seu CPF: ').strip()
    cpf = int(cpfs)
    menu = input(
        f'Seja bem vindo(a) {nome}! Em que podemos ajudar?\n[1] Sou doador.\n[2] Gostaria de receber doações.\nResposta: ').strip()
    while menu not in '1' == True or menu not in '2' == True:
        print(f'Desculpa não pude entender. {nome} poderia tentar de novo?')
        menu = input('[1] Sou doador.\n[2] Gostaria de receber doações.\nResposta: ').strip()
    if menu in '1':
        menu1 = input('Certo! Como podemos te ajudar?\n [1] Quero doar roupas\n [2] Consultar pontos de doação.\n[3] Duvidas sobre como doar roupas!\n[4] Sair\nResposta: ')
        while menu1 not in '1' == True or menu1 not in '2' == True or menu1 not in '3' == True or menu1 not in '4' == True:
            print(f'Desculpa não pude entender. {nome} poderia tentar de novo?')
            menu1 = input('Certo! Como podemos te ajudar?\n [1] Quero doar roupas\n [2] Consultar pontos de doação.\n[3] Duvidas sobre como doar roupas!\n[4] Sair\nResposta: ')
        if menu1 in '1':
            countcolunas = 0
            while True:
                countcolunas += 1
                listaderoupas = []
                roupas = input('''Por favor informe a roupa que deseja doar com as caracteristicas essênciais da mesma (Tamanho, tipo, gênero etc...): ''')
                listaderoupas.append(roupas)
                workbook.close()
                resptest = input('Você deseja doar mais? [S/N]\nResposta: ')
                while resptest not in 'S' == True or resptest not in 'N' == True:
                    resptest = input('Você deseja doar mais? [S/N]\nResposta: ')
                if resptest in 'S':
                    print('Muito obrigado!')
                    roupas = input('''Por favor informe a roupa que deseja doar com as caracteristicas essênciais da mesma (Tamanho, tipo, gênero etc...): ''')
                elif resptest in 'N':
                    resptest2 = input('Para sair aperte [1]\nPara adicionar no banco de dados aperte [2]\nResposta: ')
                    while resptest2 not in '1' == True or resptest2 not in '2' == True:
                        resptest2 = input('Para sair aperte [1]\nPara adicionar no banco de dados aperte [2]\nResposta: ')
                    if resptest2 in '2':
                        worksheet4.write(countcolunas, 2, roupas) #AQUI PODEMOS DEFINIR MELHOR PARA APARECER NA TELA
                        countcolunas = countcolunas + 1
                        print('Registrado!')
                        break
                    elif resptest2 in '1':
                        break 
        if menu1 in '2':
            print('Os pontos de doação disponíveis são:')
            print('Rua Capitão Cruz, 1474 Bairro: Centro')
        elif menu1 in '3':
            print('''Como faço para doar roupas online?\n
            Você pode doar roupas através da nossa plataforma selecionando a opção "Sou Doador" e em seguida na opção "Quero Doar Roupas Online". Após isto, indique as roupas que deseja doar e selecione o ponto de doação mais próximo de sua residência. Basta ligar para o número 4002-8922 e informar a sua localização que um de nossos parceiros cadastrados irá buscar suas doações com um frete com um valor simbólico referente a região da cidade (Metropolitana: R$ 15,00 e Rural: R$ 25,00), independente da quantidade de itens.\n
            Como faço para doar roupas presencialmente?\n
            Basta levar seu documento com foto e cpf para uma de nossos centros de doações.\n
            A plataforma é segura?\n
            Sim, ela é totalmente segura. Quem irá buscar suas doações será um de nossos parceiros cadastrados com uma senha que aparecerá no seu celular e o mesmo deverá dizer ela para você.\n
            Há limites de roupas a serem doadas?\n
            Não, você pode doar quantas roupas quiser, sejam elas masculinas, femininas, infantis ou adultas.\n
            Vale ressaltar que as roupas devem estar em boas condições, sem grandes danos. Imagine que fosse você quem precisa usá-la.''')
        elif menu1 in '4':
            break
    elif menu in '2':
        vestuario = pandas.read_excel('banco.xlsx',sheet_name='ESTOQUE')  # MUDAR ISSO DEPOIS
        print(vestuario)
        print('Você pode comparecer em ', Endereço1, 'e solicitar as roupas desejadas!')
    resp = input('Você deseja sair? [S/N]\nResposta: ').upper()
    while resp not in 'S' == True or resp not in 'N' == True:
        resp = input('Você deseja sair? [S/N]\nResposta: ').upper()
    if resp in 'S':
        break
print('\nAguardaremos seu retorno!')
workbook.close()

#O código está funcionando, algumas funções podem ainda ser melhor incrementadas