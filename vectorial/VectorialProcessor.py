from ..basics.BasicProcessor import BasicProcessor

class VectorialProcessor(BasicProcessor):
    def __init__(self, terms):
        super().__init__(terms)

    def ProcessDocument(self, document):
        return [sum([1 if j == i else 0 for j in document]) for i in self.terms]