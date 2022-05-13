
class Consult:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.relevant = []
        self.tokens = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.content