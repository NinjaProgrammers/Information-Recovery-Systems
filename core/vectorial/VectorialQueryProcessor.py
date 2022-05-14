from core.basics import BasicQueryProcessor
from core.basics import Vectorizer

class VectorialQueryProcessor(BasicQueryProcessor):
    def __init__(self, vectorizer: Vectorizer):
        super().__init__(vectorizer)

    def ProcessQuery(self, query):
        query.tokens = self.vectorizer(str(query))
        return query.tokens
