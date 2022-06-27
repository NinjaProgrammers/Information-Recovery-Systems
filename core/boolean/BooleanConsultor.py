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
                return a / (a + b + c) - (1 - a / (a + c))

            documents.sort(key=cmp, reverse=True)
            return documents
