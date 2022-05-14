from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.boolean import BooleanModel
from core.fileProcessing.Loader import LoadCranDocuments


def InitializeBooleanModel():
    documents = LoadCranDocuments()
    vectorizer = Vectorizer([str(i) for i in documents], True)
    storage = InMemoryStorage()
    boolean = BooleanModel(storage, vectorizer)
    for d in documents:
        boolean.AddDocument(d)
    return boolean
