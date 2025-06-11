filename = 'corpus.txt'

def import_as_tuple(filename):
    tuples = []
    with open(filename) as file:
        for line in file:
            word, freq = line.strip().split(',')
            tuples.append((word, freq)) 
            
            
    return tuples

print(import_as_tuple(filename))