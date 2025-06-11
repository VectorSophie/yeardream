from user import User

class Post:

    def __init__(self, author, content):

        self.author = author
        self.content = content
        self.comments = []
        self.likes = 0
        
me = User("Jack")

my_post = Post(me, "kys")