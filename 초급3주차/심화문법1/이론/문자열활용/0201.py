trump_tweets = ['america', 'is', 'back', 'and', 'we', 'are', 'coming', 'back', 'bigger', 'and', 'better', 'and', 'stronger', 'than', 'ever', 'before']

def make_new_list(text):
    new_list = []
    for t in text:
        if t.startswith('b'):
            new_list.append(t)
    
    return new_list

new_list = make_new_list(trump_tweets)
print(new_list)