
class BasicQueryProcessor:
    def __init__(self, terms):
        self.terms = terms

    def ProcessQuery(self, query):
        raise NotImplementedError()