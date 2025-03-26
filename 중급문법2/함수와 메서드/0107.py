def uniqueMorseRepresentation(words):
    alphabeta = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    alpha_dict = dict(zip(alphabeta,morse_code))

    changed_words = set()
    for word in words:
        morse_word = ''.join(alpha_dict[i] for i in word)  
        changed_words.add(morse_word)

    return len(changed_words)

word = ["gin","zen","gin","msg"]
print(uniqueMorseRepresentation(word))