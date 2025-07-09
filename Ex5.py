def count_diagonals(n):
    return n * (n - 3) // 2

# 10 sides polygons
n = 10
diagonals = count_diagonals(n)
print(f"The diagonal number of polygons {n} edge:", diagonals)