import numpy as np
from core.basics.BasicConsultor import BasicConsultor


class BooleanConsultor(BasicConsultor):
    def Consult(self, documents, query, relaxed=None):
        relevant = []
        if relaxed is None:
            relevant = [doc for doc in documents if np.array_equal(doc.tokens, query)]
        else:
            for doc in documents:
                a = len(np.intersect1d(doc.tokens, query))
                b = len(np.setdiff1d(doc.tokens, query))
                c = len(np.setdiff1d(query, doc.tokens))
                if (a + 2 * c) != 0 and a / (a + 2 * c) >= relaxed: relevant.append(doc)
        return relevant
