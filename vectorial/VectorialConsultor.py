from basics.BasicConsultor import BasicConsultor
from basics.Utils import angle


class VectorialConsultor(BasicConsultor):

    def Consult(self, documents, query):
        cmp = lambda x: angle(x.tokens, query)
        documents.sort(key=cmp, reverse=True)
        return documents
