
class Document:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.tokens = None

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.__str__()


class CranDocument(Document):
    def __init__(self, id, title, author, bibliography, content):
        super().__init__(id, content)
        self.title = title
        self.author = author
        self.bibliography = bibliography

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'.T: {self.title}\n.A: {self.author}\n' \
               f'.B: {self.bibliography}\n.C: {self.content}'