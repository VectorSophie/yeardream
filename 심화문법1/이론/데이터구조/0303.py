pairs = [
    ('time', 8),
    ('the', 15),
    ('turbo', 1),
]

def get_freq(pair):
    return pair[1]

def sort_by_frequency(pairs):
    return sorted(pairs, key=get_freq)

print(sort_by_frequency(pairs))