from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.fileProcessing.Loader import LoadCranDataset, LoadIMDBDataset, LoadNewsgroupDataset
from core.vectorial.VectorialModel import VectorialModel


def InitializeVectorialModel():
    # documents, _ = LoadCranDataset("./Test Collections/Cran/")
    # documents = LoadIMDBDataset("./Test Collections/imdb/")
    documents = LoadNewsgroupDataset("./Test Collections/Newsgroups/")
    vectorizer = Vectorizer([str(i) for i in documents])
    storage = InMemoryStorage()
    vectorial = VectorialModel(storage, vectorizer)
    for d in documents:
        vectorial.AddDocument(d)
    return vectorial
