from InMemoryStorage import InMemoryStorage
from boolean.BooleanModel import BooleanModel

def MeasureBooleanModel(documents, consults, features):
    booleanStorage = InMemoryStorage()
    booleanModel = BooleanModel(booleanStorage, features)
    for i in documents: booleanModel.AddDocument(i)

    precisionMeasures, recallMeasures = [], []
    for q in consults:
        relevant = [i[1] for i in q.relevant if i[2] == 1]
        recovered = booleanModel.Consult(q, relaxed=3)

        rr = sum((1 if i.id in relevant else 0 for i in recovered))
        precisionMeasures.append((rr + 1) / (len(recovered) + 1))
        recallMeasures.append((rr + 1) / (len(relevant) + 1))
    return precisionMeasures, recallMeasures # mean: 0.6320939904124775 0.8667830687830688







