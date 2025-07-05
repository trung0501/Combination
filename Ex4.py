# Hàm tính giai thừa
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

group1_positions = 4
group1_permutations = factorial(2)

group2_positions = 3
group2_permutations = factorial(3)

# Tổng số cách
total_ways = group1_positions * group1_permutations * group2_positions * group2_permutations

print("Total number of choices:", total_ways)