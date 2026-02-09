def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
      #cria a linha i  
        linha = []
        for j in range(num_colunas):
            valor = input(f"Digite o valor para a posição ({i}, {j}): ")
            linha.append(valor)
        matriz.append(linha)
    return matriz
def le_matriz(matriz):
    for linha in matriz:
        print(linha)
num_linhas = int(input("Digite o número de linhas: "))
num_colunas = int(input("Digite o número de colunas: "))
valor = input("Digite o valor para preencher a matriz: ")
matriz = cria_matriz(num_linhas, num_colunas, valor)
print("Matriz criada:", le_matriz(matriz))
    
  