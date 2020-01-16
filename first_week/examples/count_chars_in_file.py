"""
Count the occurences of each character in a file full of text.
Also measure the time of execution.

This example introduces a new keyword: `with`, check online documentation for this.
"""

import time

filename = 'resources/chapter1.txt'
start_time = time.time()

with open(filename) as f:
    text = f.read()
    occurences = dict()
    characters = set(text)
    for char in characters:
        occurences[char] = text.count(char)

end_time = time.time()
print("Found the occurences in", end_time - start_time, "seconds.")
for k, v in sorted(occurences.items()):
    print(k, ':', v)
