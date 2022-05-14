from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.fileProcessing.Loader import LoadCranDocuments
from core.vectorial.VectorialModel import VectorialModel


def InitializeVectorialModel():
    documents = LoadCranDocuments()
    vectorizer = Vectorizer([str(i) for i in documents])
    storage = InMemoryStorage()
    vectorial = VectorialModel(storage, vectorizer)
    for d in documents:
        vectorial.AddDocument(d)
    return vectorial
