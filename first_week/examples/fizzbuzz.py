"""
Create a function that accepts as input a positive integer 'n'. For all integers up till 'n', print an output which:
1. If 'n' is a multiple of 3, print "fizz"
2. If 'n' is a multiple of 5, print "buzz"
3. else the number itself
"""


def fizzbuzz(n):
    d = {3: "fizz", 5: "buzz", 7: "gazz"}
    for i in range(n + 1):
        output = ''
        for k, v in d.items():
            if i % k == 0:
                output += v

        if not output:
            output = i
        print(output)

fizzbuzz(105)
