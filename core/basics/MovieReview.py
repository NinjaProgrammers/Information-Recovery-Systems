
class MovieReview:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.tokens = None

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.__str__()