words = [
    'apple',
    'banana',
    'alpha',
    'bravo',
    'cherry',
    'charlie',
]

def filter_by_prefix(words, prefix):
    return [word for word in words if word.startswith(prefix)]

a_words = filter_by_prefix(words, 'a')
print(a_words)
