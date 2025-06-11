class Article():
    likes = 0
    content = ""
    hashtag = []
    
    def remove(self):
        self.likes = 0
        self.content = ""
        self.hashtag = []
    
    def like_article(self):
        self.likes += 1

insta = Article()
insta.content = "열심히 코딩 공부 하는 중"
insta.hashtag = ['엘리스', '체셔']
insta.like_article()
insta.like_article()
insta.like_article()

print(insta.content)
print(insta.hashtag)
print(insta.likes)

insta.remove()

print(insta.content)
print(insta.hashtag)
print(insta.likes)