
class Document:
    def __init__(self, id, title, author, bibliography, content):
        self.id = id
        self.title = title
        self.author = author
        self.bibliography = bibliography
        self.content = content
        self.representation = None