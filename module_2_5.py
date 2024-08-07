def get_matrix(n, m, value):
    matrix = []
    for n in range(n):
        matrix.append([])
    for i in range(m):
       matrix[0].append(value)
       matrix[1].append(value)
       matrix[-1].append(value)
       matrix[-2].append(value)
       if [42, 42, 42, 42, 42] in matrix[-2]:
           matrix[-2].remove([42, 42, 42, 42, 42])

    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
