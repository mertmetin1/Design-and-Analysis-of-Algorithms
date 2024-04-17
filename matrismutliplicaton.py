def add_matrices(matrix1, matrix2):
    # Sonuç matrisi için boş bir matris oluştur
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Matrislerin elemanlarını topla
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result





# Example matrices A and B
A = [[6981, 22, 3],
     [445, 5, 6123],
     [7123, 843, 990]]

B = [[9123, 8, 7123],
     [612, 543, 4],
     [3123, 234, 113]]

result_matrix = add_matrices(A, B)
for row in result_matrix:
    print(row)
