from utils import go_to

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content


class LinkPost(Post):
    def __init__(self, author, content, url):
        super().__init__(author, content)

        valid_url = url.startswith("http://") or url.startswith("https://")
        if not valid_url:
            raise ValueError("통과시켜줘")
        self.url = url

    def on_click(self):
        go_to(self.url)