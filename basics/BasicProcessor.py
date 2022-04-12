class BasicProcessor:
    def __init__(self, terms):
        self.terms = terms


    def ProcessDocument(self, document):
        raise NotImplementedError()