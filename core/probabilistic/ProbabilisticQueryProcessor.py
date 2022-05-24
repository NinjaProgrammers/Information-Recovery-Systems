from core.basics.BasicQueryProcessor import BasicQueryProcessor
from numpy import float32


class ProbabilisticQueryProcessor(BasicQueryProcessor):
    def __init__(self, vectorizer):
        super().__init__(vectorizer)

    def ProcessQuery(self, query):
        query.tokens = self.vectorizer.CountTransform(str(query))
        return query.tokens.astype(float32)