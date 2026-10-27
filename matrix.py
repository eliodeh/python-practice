def math_add(a, b):
    rows, cols = len(a), len(b[0])
    assert len(b) == rows and len(b[0]) == cols
    return [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print(math_add(a, b))