from core.basics.BasicConsultor import BasicConsultor
from core.basics.Utils import angle
from core.basics.Retroalimentation import Retroalimentation
import numpy as np


class VectorialConsultor(BasicConsultor, Retroalimentation):

    def Consult(self, documents, query):
        cmp = lambda x: angle(x.tokens, query)
        documents.sort(key=cmp, reverse=True)
        return documents

    def ReConsult(self, documents, query, relevant, irrelevant):
        if relevant is None or irrelevant is None:
            return self.Consult(documents, query)

        alpha, beta, gamma = 1, 0.7, 0.3
        if len(relevant) == 0: rcentroid = np.zeros(len(query))
        else: rcentroid = np.sum([d for d in relevant], axis=0) / len(relevant)

        if len(irrelevant) == 0: icentroid = np.zeros(len(query))
        else: icentroid = np.sum([d for d in irrelevant], axis=0) / len(irrelevant)

        newquery = alpha * query + beta * rcentroid - gamma * icentroid
        return self.Consult(documents, newquery)
