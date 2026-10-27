def dot(a, b):
    assert len(a) == len(b)
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total 
print(dot([1, 2, 3], [4, 5, 6]))