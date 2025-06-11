trump_tweets = [
    "FAKE NEWS - A TOTAL POLITICAL WITCH HUNT!",
    "Any negative polls are fake news, just like the CNN, ABC, NBC polls in the election.",
    "The Fake News media is officially out of control.",
]
 
def lowercase_all_characters(text):
    processed_text = []
    for i in text:
        processed_text.append(i.lower())
    
    return processed_text

print('\n'.join(lowercase_all_characters(trump_tweets)))