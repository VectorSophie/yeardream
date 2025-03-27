from utils import User, Post

class Reaction:

    def __init__(self, reaction_type, post, user):
        if reaction_type not in ["LIKE", "LOVE", "HAHA", "SAD", "ANGRY", "WOW"]:
            raise ValueError("lol")
        if not isinstance (post, Post):
            raise TypeError("post stuff.")
        if not isinstance (user, User):
            raise TypeError("be a user.")

        self.reaction_type = reaction_type
        self.post = post
        self.user = user

        post.reactions.append(self)

class Like(Reaction):
    def __init__(self, post, user):
        super().__init__("LIKE", post, user)
        post.positive_reactions += 1

class Angry(Reaction):

    def __init__(self, post, user):
        super().__init__("ANGRY", post, user)
        post.negative_reactions += 1

like = Like(Post("Hello"), User("me"))
angry = Angry(Post("Nah"), User("me"))
print(like.post.content)