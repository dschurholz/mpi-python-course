"""
Count all words in a sentence (string). Number of words is 11.
"""

separator = [" ", "\n", "\t", ".", "!", "?", "-"]
sentence = """  This is! sasa.21    a . big

    fat sentence 
    full of words"""

num_words = 0
is_word = False
for i, x in enumerate(sentence):
    if x not in separator and not is_word:
        is_word = True
    if x in separator and is_word:
        is_word = False
        num_words += 1
if is_word:
    num_words += 1

print(num_words)
