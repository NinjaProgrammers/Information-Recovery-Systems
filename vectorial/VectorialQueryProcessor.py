from basics.BasicQueryProcessor import BasicQueryProcessor
from basics.Utils import normalize

class VectorialQueryProcessor(BasicQueryProcessor):
    def __init__(self, terms):
        super().__init__(terms)

    def ProcessQuery(self, query):
        arr = [sum([1 if j == i else 0 for j in query]) for i in self.terms]
        arr = normalize(arr)
