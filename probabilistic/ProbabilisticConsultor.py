from basics.BasicConsultor import BasicConsultor
from basics.Utils import dot

class ProbabilisticConsultor(BasicConsultor):

    def Consult(self, documents, queryRSV):
        return dot(documents, queryRSV)
