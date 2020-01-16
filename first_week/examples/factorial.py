"""
Calculate the factorial of a number 'n'. (n!) 6! = 720
"""

n = 6
factorial = 1

if n < 0:
    raise ValueError("Factorial of negative numbers can't be calculated.")

for i in range(1, n + 1):
    factorial *= i

print(factorial)
