




#Matrizes:
# Matrizes são representadas como listas de listas.
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# print(matriz[1][2])  # Acessando o elemento na linha 1, coluna 2

#///////////////////////////////////////////////////////////////////////////////////////

# Soma de vetores
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
soma_vetores = [a + b for a, b in zip(vetor1, vetor2)]

# Produto de matrizes
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
produto_matrizes = [[sum(x * y for x, y in zip(row, col)) for col in zip(*matriz2)] for row in matriz1]

# Transposição de uma matriz
matriz_transposta = [[row[i] for row in matriz] for i in range(len(matriz[0]))]

# print(matriz_transposta)

import numpy as np

# Criando arrays (equivalentes a vetores/matrizes) com NumPy
vetor_numpy = np.array([1, 2, 3])
matriz_numpy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Operações com NumPy
soma_vetores_numpy = vetor_numpy + vetor_numpy
produto_matrizes_numpy = np.dot(matriz_numpy, matriz_numpy)
print(produto_matrizes_numpy)
