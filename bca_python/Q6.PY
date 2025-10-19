def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result

A1 = [[1, 2], [3, 4]]
A2 = [[2, 0], [1, 2]]
A3 = [[1, 1], [0, 1]]

temp = multiply_matrices(A1, A2)
final = multiply_matrices(temp, A3)

print("Final Result:")
for row in final:
    print(row)
