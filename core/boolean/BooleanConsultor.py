import numpy as np
from core.basics.BasicConsultor import BasicConsultor


class BooleanConsultor(BasicConsultor):
    def Consult(self, documents, query, relaxed=None):
        if not relaxed:
            return [doc for doc in documents if not any(np.setdiff1d(query, doc.tokens))]
        else:
            def cmp(doc):
                a = len(np.intersect1d(doc.tokens, query))
                b = len(np.setdiff1d(doc.tokens, query))
                c = len(np.setdiff1d(query, doc.tokens))
                if a + 2 * c == 0: return 0
                return 2 * a / (2 * a + b + c)

            documents.sort(key=cmp, reverse=True)
            return documents
