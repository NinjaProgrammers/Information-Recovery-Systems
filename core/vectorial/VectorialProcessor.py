from core.basics.Vectorizer import Vectorizer
from core.basics.BasicProcessor import BasicProcessor


class VectorialProcessor(BasicProcessor):
    def __init__(self, vectorizer: Vectorizer):
        super().__init__(vectorizer)

    def ProcessDocument(self, document):
        document.tokens = self.vectorizer(str(document))
        return document.tokens