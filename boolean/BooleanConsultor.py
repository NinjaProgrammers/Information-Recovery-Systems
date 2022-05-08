from basics.BasicConsultor import BasicConsultor

class BooleanConsultor(BasicConsultor):
    def Consult(self, documents, query, relaxed=None):
        if relaxed is None: return [i for i in documents if i in query]
        relevant = []
        for doc in documents:
            mx = relaxed + 1
            for con in query:
                temp = sum((1 if not i in doc else 0 for i in con))
                mx = min(mx, temp)
            if mx <= relaxed: relevant.append(doc)
        return relevant
