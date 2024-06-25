import time
import math

def bruteForce(coef, n, x):
    sum = 0.0
    for i in range(n + 1):
        sum += coef[i] * math.pow(x, i)
    return sum

def hornersRule(coef, n, x):
    result = coef[n]
    for i in range(n - 1, -1, -1):
        result = result * x + coef[i]
    return result

# Main Code
n = int(input("Enter the degree of the polynomial: "))
coef = [0] * (n + 1)

print("Enter the coefficients from highest degree to lowest:")
for i in range(n, -1, -1):
    coef[i] = int(input())

x = float(input("Enter the value of x: "))

start = time.time()
brute_force_result = bruteForce(coef, n, x)
end = time.time()
time_used = end - start
print(f"Brute force result: {brute_force_result:.2f}, time used: {time_used:.6f} seconds")

start = time.time()
horners_rule_result = hornersRule(coef, n, x)
end = time.time()
time_used = end - start
print(f"Horner's rule result: {horners_rule_result:.2f}, time used: {time_used:.6f} seconds")
