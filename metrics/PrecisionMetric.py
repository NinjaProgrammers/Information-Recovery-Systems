from statistics import mean
from InMemoryStorage import InMemoryStorage
from boolean.BooleanModel import BooleanModel
from vectorial.VectorialModel import VectorialModel
from probabilistic.ProbabilisticModel import ProbabilisticModel

from fileProcessing.FileProcessing import Vectorizer


def MeasurePrecisionForBooleanModel(documents, consults):
    vectorizer = Vectorizer([str(i) for i in documents])
    for i in documents: i.tokens = list(vectorizer.Analyze(str(i)))
    for i in consults: i.tokens = list(vectorizer.Analyze(str(i)))

    booleanStorage = InMemoryStorage()
    booleanModel = BooleanModel(booleanStorage, vectorizer.Features())
    for i in documents: booleanModel.AddDocument(i)
    precisionMeasures = []
    for q in consults:
        relevant = [i[1] for i in q.relevant if i[2] == 1]
        if len(relevant) == 0: continue
        recovered = booleanModel.Consult(q)

        rr = len([1 for i in recovered if i.id in relevant])
        precisionMeasures.append((rr + 1) / (len(recovered) + 1))
    return precisionMeasures







