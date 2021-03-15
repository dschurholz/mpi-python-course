
s = "hello world and practice makes perfect and hello world again"
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
