import numpy as np

def bayes_theorem():

    p_spam = 8/20

    p_confirm_spam = 5/8

    p_ham = 12/20

    p_confirm_ham = 2/12

    p_spam_confirm = (p_confirm_spam*p_spam) / (7/20)
    
    p_ham_confirm = (p_confirm_ham*p_ham) / (7/20)
    
    return p_spam_confirm, p_ham_confirm

def main():
    
    p_spam_confirm, p_ham_confirm = bayes_theorem()
    
    print("P(spam|confirm) = ",p_spam_confirm, "\nP(ham|confirm) = ",p_ham_confirm, "\n")

    value = [p_spam_confirm, p_ham_confirm]
    
    if p_spam_confirm > p_ham_confirm:
        print( round(value[0] * 100, 2), "% 의 확률로 스팸 메일에 가깝습니다.")
    else :
        print( round(value[1] * 100, 2), "% 의 확률로 일반 메일에 가깝습니다.")


if __name__ == "__main__":
    main()
