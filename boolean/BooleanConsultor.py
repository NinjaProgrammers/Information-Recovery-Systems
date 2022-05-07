from basics.BasicConsultor import BasicConsultor

class BooleanConsultor(BasicConsultor):
    def Consult(self, documents, query, relaxed=None):
        if relaxed is None: return [i for i in documents if i in query]
        relevant = []
        for i in documents:
            mx = len(i)
            for j in query:
                temp = sum((1 if (x == 0 and y == 1) else 0 for x, y in zip(i, j)))
                mx = min(mx, temp)
            if mx <= relaxed: relevant.append(i)
        return relevant
