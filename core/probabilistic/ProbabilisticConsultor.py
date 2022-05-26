from core.basics.BasicConsultor import BasicConsultor
import numpy as np
from math import log2

class ProbabilisticConsultor(BasicConsultor):
    def __init__(self, df, n):
        self.df = df
        self.n = n
        self.vocabulary = len(self.df)
        self.eps = 1e-9

    def Consult(self, documents, query, size=None, retroalimentation=None):
        assert (retroalimentation is None or (isinstance(retroalimentation, int) and isinstance(size, int)))
        pi = np.ones(self.vocabulary) * 0.5
        ri = self.df / self.n

        iterations = 1 if retroalimentation is None else retroalimentation
        for it in range(iterations):
            rsv = np.array([self.RSV(p, r) for p, r in zip(pi, ri)])

            cmp = lambda doc: np.sum(np.take(rsv, np.intersect1d(doc.tokens, query)))
            documents.sort(key=cmp, reverse=True)
            if not retroalimentation: return documents

            vi = np.zeros(self.vocabulary)
            for doc in documents[:size]:
                vi[doc.tokens] += 1
            pi = vi / size
            ri = (self.df - vi + self.eps) / (self.n - size + self.eps)

        return documents

    def RSV(self, p, r):
        if min([p, r, 1 - p, 1 - r]) < self.eps : return 0.0
        return log2((p * (1 - r) + self.eps) / (r * (1 - p)) + self.eps)