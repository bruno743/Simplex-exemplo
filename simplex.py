''' determina em qual linha está a variável que sairá da base '''
def teste(matriz, coluna):
    sai_base = 0                # variável que ajudará no teste da razão
    linha = -1                  # inicializando variável linha

    for i in range(len(matriz)):            # inicializando variável com com a razão entre o valor de b[i] e x[i][coluna]
        if(matriz[i][coluna] != 0):
            sai_base = matriz[i][len(matriz[0])-1]/matriz[i][coluna]
            break

    for i in range(len(matriz)):
        if(matriz[i][coluna] != 0 and matriz[i][len(matriz[0])-1]/matriz[i][coluna] <= sai_base):
            sai_base = matriz[i][len(matriz[0])-1]/matriz[i][coluna]
            linha = i
    
    return linha

''' pivoteamento da nova base em X[linha][coluna]'''
def troca_de_base(matriz, linha, coluna, fobjetivo):
    mult = fobjetivo[coluna]                # variáveis auxiliares para o pivoteamento
    div = matriz[linha][coluna]

    for i in range(len(matriz[0])):         # fazendo o pivô ser igual a 1 e atualizando função objetivo
        matriz[linha][i] /= div
        fobjetivo[i] -= matriz[linha][i]*mult
    
    for i in range(len(matriz)):                        # zerando elementos acima e abaixo do pivô
        if((i != linha) and (matriz[i][coluna] != 0)):
            mult = matriz[i][coluna]
            for j in range(len(matriz[0])):
                matriz[i][j] -= matriz[linha][j]*mult

''' determina qual variável não-básica entrará na base '''
def entra_base(vetor, m):
    if m == '0':
        valor_min = min(vetor[0:len(vetor) - 1], key=float)
        if (valor_min < 0):
            return vetor.index(valor_min)       # coluna da variável candidata
        else:
            return -1
    if m == '1':
        valor_max = max(vetor[0:len(vetor) - 1], key=float)
        if (valor_max > 0):
            return vetor.index(valor_max)       # coluna da variável candidata
        else:
            return -1

entrada = open('PPL.txt', 'r').readlines()
linhas = []
matriz = []
fobjetivo = []
n = 0

''' dividindo o arquivo lido em função objetivo e matriz de restrições '''
for line in entrada:
    for i in line.split(' '):
        linhas.append(float(i))
    if n <= 0:
        fobjetivo = linhas            # função objetivo
    else:
        matriz.append(linhas)         # matriz de restrições
    linhas = []
    n+=1

print("Essa é a matriz:")
for i in range(len(matriz)):
    print(matriz[i])

print("Essa é a função objetivo a ser minimizada:")
print(fobjetivo, "\n")

question = 's'
''' aplicando o simplex (+ou-) '''
max_min = input("Digite 1 para maximização e 0 para minimização:\n")
while(question != 'f'):
    if entra_base(fobjetivo, max_min) < 0:
        print("Fim!")
        break

    troca_de_base(matriz, teste(matriz, entra_base(fobjetivo, max_min)), entra_base(fobjetivo, max_min), fobjetivo)

    for i in range(len(matriz)):
        print(matriz[i])

    print("\n", fobjetivo)

    question = input("continuar: 's', parar: 'f'.\n")