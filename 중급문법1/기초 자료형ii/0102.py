words = ['i', 'have', 'a', 'pen', 'i', 'have', 'pineapple', 'i', 'have', 'an', 'apple', 'pen']

words.pop(4)
words.pop(4)
words.pop(5)
words.pop(5)
words.pop(5)

lyrics = ' '.join(words)

print(lyrics)

print(lyrics.count('p'))