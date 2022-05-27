from core.InMemoryStorage import InMemoryStorage
from core.probabilistic.ProbabilisticModel import ProbabilisticModel
from time import time

def MeasureProbabilisticModel(documents, consults, vectorizer):
    storage = InMemoryStorage()
    model = ProbabilisticModel(storage, vectorizer)
    for i in documents: model.AddDocument(i)

    precisionMeasures, recallMeasures, mapMeasures, timeMeasures = [], [], [], []
    for q in consults:
        relevant = [i[1] for i in q.relevant]
        begTime = time()
        ranking = model.Consult(q, size=20, retroalimentation=20)
        timeMeasures.append(time() - begTime)
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
    return precisionMeasures, recallMeasures, mapMeasures, timeMeasures
    # 0.3979382167903273 0.3979382167903273 0.22976914152516625 without retro
    # 0.36017291587596656 0.36017291587596656 0.16871535331529455 retro=10