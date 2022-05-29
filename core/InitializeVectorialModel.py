from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.fileProcessing.Loader import LoadCranDataset, LoadIMDBDataset, LoadNewsgroupDataset
from core.vectorial.VectorialModel import VectorialModel


def InitializeVectorialModel():
    documents, _ = LoadCranDataset("./Test Collections/Cran/")
    # documents = LoadIMDBDataset("./Test Collections/imdb/")
    # documents = LoadNewsgroupDataset("./Test Collections/Newsgroups/")
    vectorial = VectorialModel(documents)
    return vectorial
