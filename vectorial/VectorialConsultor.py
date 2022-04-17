from ..basics.BasicConsultor import BasicConsultor
from ..basics.Utils import angle

class VectorialConsultor(BasicConsultor):

    def Consult(self, documents, query):
        cmp = lambda x: angle(x, query)
        return sorted(documents, key=cmp, reverse=True)
