from basics.BasicProcessor import BasicProcessor
from math import log2

class ProbabilisticProcessor(BasicProcessor):
    def __init__(self, vectorizer):
        super().__init__(vectorizer)

    def ProcessDocument(self, document):
        document.tokens = self.vectorizer.CountTransform(str(document))
        return document.tokens
