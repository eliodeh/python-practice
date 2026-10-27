def vector_add(a, b):
    assert len(a) == len(b), "vectors must be same length"
    return [a[i] + b[i] for i in range(len(a))]
print(vector_add([1, 2, 3], [4, 5, 6]))