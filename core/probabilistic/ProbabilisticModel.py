from math import log2

from numpy import float32

from core.probabilistic.ProbabilisticProcessor import ProbabilisticProcessor
from core.probabilistic.ProbabilisticQueryProcessor import ProbabilisticQueryProcessor
from core.basics.BasicModel import BasicModel
from core.basics.BasicStorage import BasicStorage
from core.probabilistic.ProbabilisticConsultor import ProbabilisticConsultor


class ProbabilisticModel(BasicModel):
    def __init__(self, storage: BasicStorage, vectorizer):
        consultor = ProbabilisticConsultor()
        processor = ProbabilisticProcessor(vectorizer)
        queryProcessor = ProbabilisticQueryProcessor(vectorizer)
        super().__init__(storage, vectorizer, consultor, processor, queryProcessor)
        self.eps = 1e-18

    def Consult(self, query, size=None, retroalimentation=False):
        assert(not retroalimentation or isinstance(size, int))
        print("retroalimentation on")

        documents = self.storage.GetAllDocuments()
        processedQuery = self.queryProcessor.ProcessQuery(query)
        pi, ri = self.GetParameters()

        iterations = 5 if retroalimentation else 1
        relevant = documents
        for it in range(iterations):
            newQuery = processedQuery.copy()
            for i, index in enumerate(processedQuery.indices):
                newQuery.data[i] *= self.RSV(pi[index], ri[index])
            relevant = self.consultor.Consult(documents, newQuery)

            vi = [0] * len(pi)
            for d in relevant[:size]:
                for f in d.tokens.indices:
                    vi[f] += 1
            for i in range(len(pi)):
                pi[i] = vi[i] / size
                ri[i] = (self.vectorizer.df[i] - vi[i] + self.eps) / (self.vectorizer.N - size + self.eps)

        if size is None or size >= len(relevant): return relevant
        else: return relevant[: size]

    def GetParameters(self):
        ri = [i / self.vectorizer.N for i in self.vectorizer.df]
        pi = [0.5 for _ in range(len(self.vectorizer.Features()))]
        return pi, ri
        #return [log2((p * (1 - r) ) / (r * (1 - p))) for p, r in zip(pi, ri)]

    def RSV(self, p, r):
        return log2((p * (1 - r) + self.eps) / (r * (1 - p)) + self.eps)
