"""
This question solution introduces the `input` which allows you to input sentences from the console.
Use input? in a console to see how to use it.
Execute the file and input your sentences in the console.
"""

lines = []
print("Enter a sentece and press Enter, press Enter two times to finish the execution.")
while True:
    s = input("Input a sentence:\n")
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print(sentence)
