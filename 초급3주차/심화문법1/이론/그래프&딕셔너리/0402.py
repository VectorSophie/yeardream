from operator import itemgetter
from collections import Counter
from string import punctuation
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def import_corpus(filename):

    corpus = []
    
    with open(filename) as file:
        for line in file: 
            word, freq = line.strip().split(',') 
            corpus.append((word, int(freq))) 
    
    return corpus 

def create_corpus(filenames):
    
    words = []
    
    for filename in filenames:
        with open(filename) as file:
            content = file.read().strip()    
                    
            
            for symbol in punctuation:
                content = content.replace(symbol, '') 
            words += content.split() 
    
    corpus = Counter(words)
    return list(corpus.items())

def filter_by_prefix(corpus, prefix):

    return [(word, freq) for word, freq in corpus if word.startswith(prefix)] 


def most_frequent_words(corpus, number):
    
    return sorted(corpus, key=itemgetter(1), reverse=True)[:number] 
    

def draw_frequency_graph(corpus):
    pos = range(len(corpus))
    
    words = [tup[0] for tup in corpus]
    freqs = [tup[1] for tup in corpus]
    
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    plt.bar(pos, freqs, align='center')
    
    plt.xticks(pos, words, rotation='vertical', fontproperties=font)

    plt.title('단어 별 사용 빈도', fontproperties=font)
    
    plt.ylabel('빈도', fontproperties=font)
    
    plt.tight_layout()

    plt.savefig('graph.png')
    elice_utils.send_image('graph.png')

def main(prefix=''):

    corpus = import_corpus('corpus.txt')
    
    prefix_words = filter_by_prefix(corpus, prefix)
    
    top_ten = most_frequent_words(prefix_words, 10)
    
    draw_frequency_graph(top_ten)
    
    alice_files = ['alice/chapter{}.txt'.format(chapter) for chapter in range(1, 6)]
    alice_corpus = create_corpus(alice_files)
    
    top_ten_alice = most_frequent_words(alice_corpus, 10)
    draw_frequency_graph(top_ten_alice)

if __name__ == '__main__':
    main()