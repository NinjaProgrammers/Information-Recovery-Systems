from ..basics.BasicProcessor import BasicProcessor
from math import log2

class ProbabilisticProcessor(BasicProcessor):
    def __init__(self, terms):
        super().__init__(terms)
        self.ni = [0 for _ in range(len(terms))]
        self.N = 0

    def ProcessDocument(self, document):
        for i in range(len(self.terms)):
            if self.terms[i] in document:
                self.ni[i] += 1
        self.N += 1
        return [(1 if i in document else 0) for i in self.terms]

    def GetRSV(self):
        ri = [i / self.N for i in self.ni]
        pi = [0.5 for i in range(len(self.terms))]
        return [log2((p * (1 - r)) / (r * (1 - p))) for p, r in zip(pi, ri)]

