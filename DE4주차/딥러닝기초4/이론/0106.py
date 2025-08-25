import tensorflow as tf
from tensorflow.python.keras.preprocessing.text import Tokenizer

import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

def embedding(sentence1, sentence2):
    
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(sentence1+sentence2)
    word_dict = tokenizer.word_index
    
    for k, v in word_dict.items():
        word_dict[k] = v - 1
    
    sen1 = tokenizer.texts_to_sequences(sentence1)
    sen2 = tokenizer.texts_to_sequences(sentence2)
    
    sen1 = [token[0] for token in sen1]
    sen2 = [token[0] for token in sen2]
    
    return word_dict, sen1, sen2

def one_hot(sen1, sen2, word_dict):
    
    oh_sen1 = sum(tf.one_hot(sen1, len(word_dict)))
    oh_sen2 = sum(tf.one_hot(sen2, len(word_dict)))
    
    return oh_sen1, oh_sen2

def main():
    
    sentence1 = ['나','는','오늘','저녁','에','치킨','을','먹','을','예정','입니다']
    sentence2 = ['나','는','어제', '맥주','와', '함께', '치킨','을', '먹었', '습니다']
    
    word_dict, seq_1, seq_2 = embedding(sentence1, sentence2)
    onehot_sen1, onehot_sen2 = one_hot(seq_1, seq_2, word_dict)
        
    print('리스트 요소-인덱스 딕셔너리: ', word_dict)
    
    print('\n정수값으로 변환된 sentence1:', seq_1)
    print('\n정수값으로 변환된 sentence2:', seq_2)
    
    print('\n원-핫 인코딩된 문장1:', onehot_sen1.numpy())
    print('\n원-핫 인코딩된 문장2:', onehot_sen2.numpy())
    
    return onehot_sen1, onehot_sen2

if __name__ == '__main__':
    main()