import numpy as np
from konlpy.tag import Twitter 

def load_data(path):
    with open(path, 'r') as f:
        data = f.read()
    return data

def doc2para(writing):
    
    paragraphs = []
    
    splited = writing.split('\n')
    splited=list(filter(lambda x: len(x) >0, splited))
    para = ""
    
    for sentence in splited:
        if sentence[-1] != '.':
            para += sentence
        else:
            paragraphs.append(para)
            para = ""
    
    return paragraphs


def para2sen(paragraph):
    
    sentences = []
    
    sentences = paragraph.split('.')
    
    sentences = [sentence.split('?') for sentence in sentences]
    sentences = np.array(sentences).flatten()
    sentences = [sentence.split('!') for sentence in sentences]
    sentences = np.array(sentences).flatten()
    sentences = [ sentence.replace('"','') for sentence in sentences]
    
    return sentences

def sen2words_byspace(sentence):
    
    words = []
    words = sentence.strip().split(" ")
    
    return words

def sen2morph(sentence):
    
    morphs = []
    
    analyzer = Twitter()
    morphs = analyzer.morphs(sentence)
    
    return morphs

def analyzing_morphs(sentence):
    
    analyzer = Twitter()
    
    return analyzer.pos(sentence)

def main():
    
    DATA_PATH = "./data/blood_rain.txt"
    
    blood_rain = load_data(DATA_PATH)
    paragraphs = doc2para(blood_rain)
    sentences = para2sen(paragraphs[4])
    words_byspace = sen2words_byspace(sentences[3])
    words_bymorphs = sen2morph(sentences[3])
    morphs_analyzed = analyzing_morphs(sentences[3])
    
    print("문장으로 구분된 5번째 문단: ", sentences)
    print("\n띄어쓰기로 구분된 문장 (5번째 문단의 4번째 문장): ", words_byspace)
    print("\n형태소 별로 구분된 문장 (5번째 문단의 4번째 문장): ", words_bymorphs)
    print("\n형태소와 그에 따른 품사로 분류된 문장 (5번째 문단의 4번째 문장): ", morphs_analyzed)
    
    return words_byspace, words_bymorphs, morphs_analyzed
    
if __name__=='__main__':
    main()