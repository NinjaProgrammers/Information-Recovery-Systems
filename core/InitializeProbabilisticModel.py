from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.fileProcessing.Loader import LoadCranDataset
from core.probabilistic.ProbabilisticModel import ProbabilisticModel


def InitializeProbabilisticModel():
    documents, _ = LoadCranDataset("./Test Collections/Cran/")
    vectorizer = Vectorizer([str(i) for i in documents], True)
    storage = InMemoryStorage()
    probabilistic = ProbabilisticModel(storage, vectorizer)
    for d in documents:
        probabilistic.AddDocument(d)
    return probabilistic
