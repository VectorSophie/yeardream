user_to_titles = {
    1: [271, 318, 491],
    2: [318, 19, 2980, 475],
    3: [475],
    4: [271, 318, 491, 2980, 19, 318, 475],
    5: [882, 91, 2980, 557, 35],
}
def get_user_to_num_titles(user_to_titles):
    user_to_num_titles = {}
    
    for user, titles in user_to_titles.items():
        user_to_num_titles[user] = len(titles)
    
    return user_to_num_titles
    
print(get_user_to_num_titles(user_to_titles))