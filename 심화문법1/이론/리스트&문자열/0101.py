trump_tweets = [
    'Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!',
    'Companies are giving big bonuses to their workers because of the Tax Cut Bill. Really great!',
    'MAKE AMERICA GREAT AGAIN!'
]

def date_tweet(tweet):
    for index in range(len(tweet)):
        print('2018년 1월 ' + str(index+1) + '일: ' + tweet[index])


date_tweet(trump_tweets)