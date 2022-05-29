from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.boolean.BooleanModel import BooleanModel
from core.fileProcessing.Loader import LoadCranDataset


def InitializeBooleanModel():
    documents, _ = LoadCranDataset("./Test Collections/Cran/")
    vectorizer = Vectorizer([str(i) for i in documents], True)
    storage = InMemoryStorage()
    boolean = BooleanModel(storage, vectorizer)
    for d in documents:
        boolean.AddDocument(d)
    return boolean
