def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

# Brute force method to find binomial coefficient
def binomialCoeff_bruteForce(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Dynamic programming method to find binomial coefficient
def binomialCoeff_DP(n, k):
    C = [[0 for j in range(k + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
            # Calculate value using previously stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]

# Main Code
n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

result_bruteForce = binomialCoeff_bruteForce(n, k)
result_DP = binomialCoeff_DP(n, k)

print(f"Binomial Coefficient (Brute Force): {result_bruteForce}")
print(f"Binomial Coefficient (Dynamic Programming): {result_DP}")
