from ..basics.BasicConsultor import BasicConsultor
from math import sqrt

class VectorialConsultor(BasicConsultor):

    def Consult(self, documents, query):
        cmp = lambda x: VectorialConsultor.angle(x, query)
        return sorted(documents, key=cmp, reverse=True)

    @staticmethod
    def dot(u, v):
        return sum([i * j for i, j in zip(u, v)])

    @staticmethod
    def angle(u, v):
        return VectorialConsultor.dot(u, v) / (sqrt(VectorialConsultor.dot(u, u)) * sqrt(VectorialConsultor.dot(v, v)))