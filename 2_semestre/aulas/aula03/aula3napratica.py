#{
#    "nome": "Pedro",
#    "sobrenome": "Henrique",
#    "endereco": {
#        "rua": "Av.Paulista",
#        "cidade": "são paulo",
#        "UF": "SP",
#        "CEP": "80000000"
#    },
#    "telefone": [
#        "11 99999-9999"
#        "11 99999-9998"
#   ]
#} 

#função para escrever no arquivo JSON
from curses.ascii import FF
from operator import truediv


def escrever(dicionario):
    #função 'open()' com a opção 'w' para escrita
    with open('agenda' + '.json', 'w') as f:
        #método 'dump()' insere os dados do dicionario no arquivo Json
        json.dump(dicionario, f, indent=4)
        #fecha o arquivo para não ter problema na próxima leitura
        f.close()

def ler():
    #inicializar um dicionario vazio, pois na primeira leitura
    #o arquivo ainda nãoo existe no disco.
    agenda={}
    #tratamento de exceção
    try:
        #função 'open()' com a opção 'r' para leitura
        with open ('agenda' + '.json', 'r') as f:
            #atribuir os dados do arquivo para agenda
            agenda = json.load(f)
            #fecha o arquivo para não ter problema na proxima escrita
            f.close()
            #retorna os dados para quem chamou
            return agenda
    except FileNotFoundError:
        #se o arquivo ainda não existir, cria um vazio
        escrever(agenda)
        #retorna os dados para quem chamou
        return agenda
#controle de parada
parar = False
#enquanto para for falso, faça...
while not parar:
    #receber nome na entrada do usuario
    nome = input('Entre com o nome do contato: ')
    #receber telefone na entrada do usuario
    telefone = input('Entre com o número do telefone: ')
    #ler dados do json
    dicionario = ler
    #adicionar dados
    dicionario[nome] = telefone
    #escrever dados no json
    escrever(dicionario)
    #receber s ou n na entrada do usuario
    p = input('Parar? [s/n]: ')
    #se o conteudo de p está na string 's', então é atribuindo verdadeiro para 'parar'
    if 's' in p:
        parar = true
