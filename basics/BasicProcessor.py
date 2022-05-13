from basics.Vectorizer import Vectorizer

class BasicProcessor:
    def __init__(self, vectorizer: Vectorizer):
        self.vectorizer = vectorizer


    def ProcessDocument(self, document):
        raise NotImplementedError()