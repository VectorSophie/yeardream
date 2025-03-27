from user import User

class Post:
    
    def __init__(self, author, content):

        self.author = author
        self.content = content
        
        self.likes = []

    def num_likes(self):
        return len(self.likes)

    def like(self, user):
        self.likes.append(user)
        likes_set = set(self.likes)
        self.likes = list(likes_set)

me = User("Elice")

my_post = Post("Jack", "ffff")
my_post.like(me)
print(my_post.num_likes())