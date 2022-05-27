from core.basics.BasicConsultor import BasicConsultor
from core.basics.Utils import angle
import numpy as np


class VectorialConsultor(BasicConsultor):

    def Consult(self, documents, query):
        cmp = lambda x: angle(x.tokens, query)
        documents.sort(key=cmp, reverse=True)
        return documents

    def ReConsult(self, documents, query, relevant, irrelevant):
        if relevant is None or irrelevant is None:
            return self.Consult(documents, query)

        alpha, beta, gamma = 1, 0.7, 0.3
        rcentroid = np.sum([d for d in relevant], axis=0) / len(relevant)
        icentroid = np.sum([d for d in irrelevant], axis=0) / len(irrelevant)

        newquery = alpha * query + beta * rcentroid - gamma * icentroid
        return self.Consult(documents, newquery)
