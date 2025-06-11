import matplotlib.pyplot as plt
import json
from operator import itemgetter

from elice_utils import EliceUtils
from movies import titles


def preprocess_data(filename):
    
    processed = {}
    with open(filename) as file:
        loaded = json.loads(file.read())
        for title, users in loaded.items():
            processed[int(title)] = users
        return processed


def reformat_data(title_to_users):
    
    user_to_titles = {}
    
    for title, users in title_to_users.items():
        for user in users:
            if user in user_to_titles:
                user_to_titles[user].append(title)
            else:
                user_to_titles[user] = [title]
    
    return user_to_titles


def get_closeness(title_to_users, title1, title2):
   
    title1_users = set(title_to_users[title1])
    title2_users = set(title_to_users[title2])
    both = len(title1_users & title2_users)
    either = len(title1_users | title2_users)
    return both / either


def predict_preference(title_to_users, user_to_titles, user, title):
    
    titles = user_to_titles[user]
    closeness = [get_closeness(title_to_users, title, title2) for title2 in titles]
    return sum(closeness) / len(closeness)


def main():
    filename = 'netflix.json'
    title_to_users = preprocess_data(filename)
    user_to_titles = reformat_data(title_to_users)
    
    lotr1 = 2452                
    lotr2 = 11521               
    lotr3 = 14240               
    
    killbill1 = 14454           
    killbill2 = 457             
    
    jurassic_park = 14312       
    shawshank = 14550           
    
    print("[유사도 측정]")
    title1 = lotr1
    title2 = killbill1
    description = "{}와 {}의 작품 성향 유사도".format(titles[title1], titles[title2])
    closeness = round(get_closeness(title_to_users, title1, title2) * 100)
    
    print("{}: {}%".format(description, closeness))
    
    username = 'elice'
    new_utt = user_to_titles.copy()
    new_utt[username] = [lotr1, lotr2, lotr3]
    
    print("[{} 유저를 위한 작품 추천]".format(username))
    preferences = [(title, predict_preference(title_to_users, new_utt, 'elice', title)) for title in title_to_users]
    preferences.sort(key=itemgetter(1), reverse=True)
    for p in preferences[:10]:
        print("{} ({}%)".format(titles[p[0]], round(p[1] * 100)))


if __name__ == "__main__":
    main()