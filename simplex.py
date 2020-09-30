''' determina em qual linha está a variável que sairá da base '''
def teste(matriz, coluna):
    sai_base = 0                # variável que ajudará no teste da razão
    linha = -1                  # inicializando variável linha

    for i in range(len(matriz)):            # inicializando variável com com a razão entre o valor de b[i] e x[i][coluna]
        if(matriz[i][coluna] != 0):
            sai_base = matriz[i][len(matriz[0])-1]/matriz[i][coluna]
            break

    for i in range(len(matriz)):
        if(matriz[i][coluna] != 0 and matriz[i][len(matriz[0])-1]/matriz[i][coluna] >=0 and matriz[i][len(matriz[0])-1]/matriz[i][coluna] <= sai_base):
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
def entra_base(vetor):
    valor_min = min(vetor[0:len(vetor) - 1], key=float)
    if (valor_min < 0):
        return vetor.index(valor_min)       # coluna da variável candidata
    else:
        return -1

def print_tablo(matriz, fobjetivo):
    print("\nEssa é a matriz:")
    text = '| '
    for i in range(len(matriz[0]) - 1):
        text += 'X{} | '.format(i + 1)

    print(text, 'b ')
    for i in range(len(matriz)):
        print('{}'.format(matriz[i]))

    print("Essa é a função objetivo a ser minimizada:")
    print(fobjetivo, "\n")

arquivo = input("Qual o arquivo do problema?")  # arquivo .txt com o problema
entrada = open(arquivo, 'r').readlines()
matriz = []
fobjetivo = []
n = 0

''' dividindo o arquivo lido em função objetivo e matriz de restrições '''
for line in entrada:
    linhas = []
    for i in line.split(' '):
        linhas.append(round(float(i), 2))
    if n <= 0:
        fobjetivo = linhas            # função objetivo
    else:
        matriz.append(linhas)         # matriz de restrições
    n+=1

print_tablo(matriz, fobjetivo)

question = 's'
''' aplicando o simplex '''
max_min = input("Digite 1 para maximização e 0 para minimização:\n")
if max_min == '1':
    fobjetivo = [i*-1 for i in fobjetivo]   # em caso de MAX Z, múltiplica-se por -1 para fazer MIN Z
while(question != 'f'):
    nova_base = entra_base(fobjetivo)
    if nova_base < 0:
        print("Sem mais variáveis candidatas a entrar na base.") # solução ótima, ou não há solução
        break

    if teste(matriz, nova_base) < 0:
        print("Solução ilimitada!")     # se não é possível uma variável sair da base, solução ilimitada
        break
    
    troca_de_base(matriz, teste(matriz, nova_base), nova_base, fobjetivo)
    print_tablo(matriz, fobjetivo)

    question = input("continuar: 's', parar: 'f'.\n") # o usuário pode decidir se a solução é ótima ao ver o tablô

if question == 'f' and entra_base(fobjetivo) < 0:
    if max_min == '1':
        print("Z =", fobjetivo[len(fobjetivo)-1])   # valor de Z ótimo
    if max_min == '0':
        print("Z =", fobjetivo[len(fobjetivo)-1]*-1)

n = 0
for i in range(len(fobjetivo)):
    if fobjetivo[i] == 0.0:
        n+=1

if n > len(matriz) and question == 'f': # em caso de solução ótima
    print("\nMúltiplas soluções!")      # se houver uma variável não-básica valendo zero, existem múltiplas soluções