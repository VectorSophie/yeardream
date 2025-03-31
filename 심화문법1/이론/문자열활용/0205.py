filename = 'corpus.txt'

def print_lines(filename):
    with open(filename) as file:
        line_number = 1
        for line in file: 

            print(line_number, line)
            line_number += 1

print_lines(filename)