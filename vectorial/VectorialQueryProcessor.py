from ..basics.BasicQueryProcessor import BasicQueryProcessor


class VectorialQueryProcessor(BasicQueryProcessor):
    def __init__(self, terms):
        super().__init__(terms)

    def ProcessQuery(self, query):
        return [sum([1 if j == i else 0 for j in query]) for i in self.terms]