source_file = "netflix.txt"

def make_dictionary(filename):
    user_to_titles = {}
    with open(filename) as file:
        for line in file:

            user, title = line.strip().split(':')
            user_to_titles[user] = title
            
        return user_to_titles

print(make_dictionary(source_file))