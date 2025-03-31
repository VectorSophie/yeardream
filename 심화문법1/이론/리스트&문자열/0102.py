trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']

def print_korea(tweet): 
    result = [] 
    for t in tweet:
        if t[0] == "k" : 
            print(t) 
    
print_korea(trump_tweets)