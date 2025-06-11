trump_tweets = [
    "i hope everyone is having a great christmas, then tomorrow it’s back to work in order to make america great again.",
    "7 of 10 americans prefer 'merry christmas' over 'happy holidays'.",
    "merry christmas!!!",
]

def remove_special_characters(text):
    processed_text = []
    for i in text:
        i = i.replace('!', '').replace(',', '').replace("'", '')
        processed_text.append(i)
    
    return processed_text

print('\n'.join(remove_special_characters(trump_tweets)))