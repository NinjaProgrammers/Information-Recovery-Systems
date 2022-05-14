from core.basics.BasicConsultor import BasicConsultor
from numpy import array_equal


class BooleanConsultor(BasicConsultor):
    def Consult(self, documents, query, relaxed=None):
        relevant = []
        if relaxed is None:
            for doc in documents:
                add = False
                for q in query:
                    add |= array_equal(doc, q)
                if add: relevant.append(doc)
        else:
            for doc in documents:
                mx = relaxed + 1
                for con in query:
                    temp = sum((1 if not i in doc else 0 for i in con))
                    mx = min(mx, temp)
                if mx <= relaxed: relevant.append(doc)
        return relevant
