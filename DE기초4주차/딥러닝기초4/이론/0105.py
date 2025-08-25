import numpy as np
from konlpy.tag import Twitter

def read_txt(path):
    
    file = open(path, 'r')
    output = str(file.read())
    
    return output

def bag_of_words(tokenized_sentences):
    
    word_dict = {}
    for word in tokenized_sentences:
        try:
            word_dict[word] += 1
        except KeyError:  
            word_dict[word] = 1
    
    return word_dict

def get_splited_doc(path):
    
    output = []
    
    text = read_txt(path)
    analyzer = Twitter()
    output = analyzer.morphs(text)
    
    return text, output

def main():
    
    PATH = "./data/text.txt"
    
    origin, splitted = get_splited_doc(PATH)
    
    print('형법 제2장 원본: ', origin)
    
    bow_criminal_law = bag_of_words(splitted)
    
    print('\n형법 제2장의 BoW: ', bow_criminal_law)
    
    return bow_criminal_law

if __name__ == "__main__":
    main()