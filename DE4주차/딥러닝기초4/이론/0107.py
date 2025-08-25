from gensim.models import word2vec
import list_file

def CBOW(sentences):
    
    model_cbow = word2vec.Word2Vec(sentences, size=300,min_count=1,window=10,sg=0)
    
    return model_cbow

def Skip_Gram(sentences):
    
    model_skipgram = word2vec.Word2Vec(sentences, size=300, min_count=1, window=10,sg=1)
    
    return model_skipgram

def main():
    
    sen1, sen2 = list_file.sen1(), list_file.sen2()
    
    sentences = [sen1, sen2]
    
    cbow = CBOW(sentences)
    skipgram = Skip_Gram(sentences)
    
    idx2word_set_cbow = cbow.wv.index2word
    idx2word_set_skipgram = skipgram.wv.index2word
    
    print('CBOW: ', idx2word_set_cbow)
    print('\nSkip-Gram: ', idx2word_set_skipgram)
    
    return idx2word_set_cbow, idx2word_set_skipgram

if __name__ == '__main__':
    main()