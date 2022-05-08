
class BasicQueryProcessor:
    def __init__(self, vectorizer):
        self.vectorizer = vectorizer

    def ProcessQuery(self, query):
        raise NotImplementedError()