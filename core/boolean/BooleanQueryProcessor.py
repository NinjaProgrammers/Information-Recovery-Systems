from core.basics.BasicQueryProcessor import BasicQueryProcessor


class BooleanQueryProcessor(BasicQueryProcessor):
    def __init__(self, vectorizer):
        super().__init__(vectorizer)

    # TODO: Process the query so it gets the user input and returns the corresponding Dijuntive Normal Form
    def ProcessQuery(self, query):
        query.tokens = self.vectorizer.CountTransform(str(query))
        return query.tokens.indices