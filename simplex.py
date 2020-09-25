''' determina em qual linha está a variável que sairá da base '''
def teste(matriz, coluna, b):
    sai_base = b                # maior elemento da matriz original
    linha = -1                  # inicializando variável linha
    for i in range(len(matriz)):
        if(matriz[i][coluna] != 0 and matriz[i][len(matriz[0])-1]/matriz[i][coluna] < sai_base):
            sai_base = matriz[i][len(matriz[0])-1]/matriz[i][coluna]
            linha = i
    
    return linha

''' pivoteamento da nova base em X[linha][coluna]'''
def troca_de_base(matriz, linha, coluna, fobjetivo):
    mult = fobjetivo[coluna]                # variáveis auxiliares para o pivoteamento
    div = matriz[linha][coluna]

    for i in range(len(matriz[0])):         # fazendo o pivô ser igual a 1
        matriz[linha][i] /= div
        fobjetivo[i] -= matriz[linha][i]*mult
    
    for i in range(len(matriz)):                        # zerando elementos acima e abaixo do pivô
        if((i != linha) and (matriz[i][coluna] != 0)):
            mult = matriz[i][coluna]
            for j in range(len(matriz[0])):
                matriz[i][j] -= matriz[linha][j]*mult

''' determina qual variável não-básica entrará na base '''
def entra_base(vetor, n_variaveis):
    return vetor.index(min(vetor[0:n_variaveis], key=int))

matriz = [[1, 0, 1, 0, 0, 3], [0, 1, 0, 1, 0, 4], [1, 2, 0, 0, 1, 9]]
fobjetivo = [-5, -2, 0, 0, 0, 0]

A = 0
for i in range(len(matriz)):        # loucura
    if(max(matriz[i], key=int) > A):
        A = max(matriz[i], key=int)

print("Essa é a matriz:")
for i in range(len(matriz)):
    print(matriz[i])

print("Essa é a função objetivo a ser minimizada:")
print(fobjetivo, "\n")

question = 's'
''' aplicando o simplex (+ou-) '''
while(question != 'f'):
    troca_de_base(matriz, teste(matriz, entra_base(fobjetivo, 2), A), entra_base(fobjetivo, 2), fobjetivo)

    for i in range(len(matriz)):
        print(matriz[i])

    print("\n", fobjetivo)

    question = input("continuar: 's', parar: 'f'.\n")