from core.basics.BasicQueryProcessor import BasicQueryProcessor


class ProbabilisticQueryProcessor(BasicQueryProcessor):
    def __init__(self, vectorizer):
        super().__init__(vectorizer)

    def ProcessQuery(self, query):
        query.tokens = self.vectorizer.CountTransform(str(query))
        return query.tokens