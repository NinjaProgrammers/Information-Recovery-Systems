from basics.BasicConsultor import BasicConsultor

class BooleanConsultor(BasicConsultor):
    def Consult(self, documents, query):
        return [i for i in documents if i in query]