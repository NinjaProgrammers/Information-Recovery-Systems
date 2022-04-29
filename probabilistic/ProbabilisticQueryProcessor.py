from basics.BasicQueryProcessor import BasicQueryProcessor

class ProbabilisticQueryProcessor(BasicQueryProcessor):
    def __init__(self, terms):
        super().__init__(terms)

    def ProcessQuery(self, query):
        return [(1 if i in query else 0) for i in self.terms]