# exemplo = [[1,2,3], [4,5,6], 7,8,9]

# #percorrendo os elementos da matriz
# for lin in range(len(exemplo)):
#     for col in range(len(exemplo[lin])):
#         print(exemplo[col][lin], end='\t')
#     print()

#cria uma matriz de numeros

# numeros = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]

# print(numeros[0:2])



# matriz = [['Nome', 'Telefone', 'Sexo'], ['Nome', 'Telefone', 'Sexo']]
# for linha in range (len(matriz)):
#     for coluna in range(len(matriz[linha])):
#         if coluna == 0:
#             matriz[linha][coluna]=input('Digite o nome: ')
#         elif coluna == 1:
#             matriz[linha][coluna] = input('Digite o telefone: ')
#         else:
#             matriz[linha][coluna] = input('Digite o sexo: ')

#importação

# from matplotlib import imread

# #leitura da img
# imagem = imread('/users/bluner/dclv766-b649323c-2b5d-493c-99c2-f2f0d08b695c.png')
# print('altura em pixel: ', end='')
# print(imagem.shape[0]) #altura
# print('Largura em pixels: ', end='')
# print(imagem.shape[1]) #largura
# print('Qtde de dimensões: ', end='')
# print(imagem.shape[2]) #dimensoes

matriz_01 = [['a00', 'a01', 'a02'], 'a10', 'a11', 'a12'],['a20', 'a21', 'a22']
elementos = [0,0,0]

for i in range(len(matriz_01)):
    for j in range(len(matriz_01)):
        if i!=j:
            elementos[i] = matriz_01[i][j]
print('Diagonal principal')
print(elementos)