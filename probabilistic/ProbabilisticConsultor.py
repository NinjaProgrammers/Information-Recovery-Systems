from basics.BasicConsultor import BasicConsultor
from basics.Utils import dot

class ProbabilisticConsultor(BasicConsultor):

    def Consult(self, documents, queryRSV):
        cmp = lambda x: dot(x.tokens, queryRSV)
        documents.sort(key=cmp, reverse=True)
        return documents
