
class Document:
    def __init__(self, id, title, author, bibliography, content):
        self.id = id
        self.title = title
        self.author = author
        self.bibliography = bibliography
        self.content = content
        self.tokens = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'.T: {self.title}\n.A: {self.author}\n' \
               f'.B: {self.bibliography}\n.C: {self.content}'