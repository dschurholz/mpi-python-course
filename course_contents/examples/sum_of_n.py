"""
Find a number `x` such that the sum from 0 to x, including it, is higher than a number `n`.
`x` should be the lowest possible number to satisfy this condition.
"""

n = 346
s = 0
i = 0
while s < n:
    i += 1
    s += i

print("The lowest number to satisfy the condition is", i, "with a sum of", s)
