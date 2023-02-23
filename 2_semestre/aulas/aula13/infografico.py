#infografico
teste = [[1,2,3], [4,5,6], [7,8,9]]
diag_princ = [0,0,0]
diag_sec = [0,0,0]

for i in range(len(teste)):
    for j in range(len(teste[i])):
        if i == j:
            diag_princ[i] = teste[i]
        if i+j == len(teste)-1:
            diag_sec[i] = teste[i][j]

print('diagonal principal')
print(diag_princ)
print('diagonal secundaria')
print(diag_sec)