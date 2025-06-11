class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.shared_users = []
        self.is_private = False

    def share(self, user):
        self.shared_users.append(user)
        

class PrivatePost(Post):
   
    def __init__(self, author, content):
        super().__init__(author, content)
        self.is_private = True

    def share(self, user):
        raise TypeError("no.")