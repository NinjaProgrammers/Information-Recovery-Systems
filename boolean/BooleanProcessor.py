from ..basics.BasicProcessor import BasicProcessor

class BooleanProcessor(BasicProcessor):
    def __init__(self, terms):
        super().__init__(terms)

    def ProcessDocument(self, document):
        return [(1 if i in document else 0) for i in self.terms]