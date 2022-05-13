from InMemoryStorage import InMemoryStorage
from vectorial.VectorialModel import VectorialModel

def MeasureVectorialModel(documents, consults, vectorizer):
    storage = InMemoryStorage()
    model = VectorialModel(storage, vectorizer)
    for i in documents: model.AddDocument(i)

    precisionMeasures, recallMeasures, mapMeasures = [], [], []
    for q in consults:
        relevant = [i[1] for i in q.relevant if i[2]]
        ranking = model.Consult(q)
        sz = len(relevant)

        founded, s = 0, 0
        for i, d in enumerate(ranking):
            if d.id in relevant:
                founded += 1
                s += founded / (i + 1)
        mapMeasures.append(s / (sz + 1))

        rr = sum([1 if i.id in relevant else 0 for i in ranking[:sz]])
        precisionMeasures.append((rr + 1) / (sz + 1))
        recallMeasures.append((rr + 1) / (len(relevant) + 1))
    return precisionMeasures, recallMeasures, mapMeasures
    # 0.4660001019570855 0.4660001019570855 0.351396020904683