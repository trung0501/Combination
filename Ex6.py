def C(n, k):
    if k == 0 or k == n:
        return 1
    res = 1
    for i in range(1, k+1):
        res *= (n - i + 1)
        res //= i
    return res

def max_orthogonal_intersections(n):
    c2 = C(n - 1, 2)            
    total_lines = n * c2       
    total_pairs = C(total_lines, 2)  

    overlap_type1 = n * (c2 - 1)     
    overlap_type2 = 5 * C(n, 3)      

    max_intersections = total_pairs - (overlap_type1 + overlap_type2)
    return max_intersections

# Enter n arbitrary
n = 5
print("The maximum number of intersections is orthogonal:", max_orthogonal_intersections(n))