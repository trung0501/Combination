def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

answer_count = combination(40, 18)
print("The number of different true/false answer combinations is:", answer_count)