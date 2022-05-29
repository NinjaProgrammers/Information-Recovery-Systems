from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.boolean.BooleanModel import BooleanModel
from core.fileProcessing.Loader import LoadCranDataset, LoadIMDBDataset, LoadNewsgroupDataset


def InitializeBooleanModel():
    documents, _ = LoadCranDataset("./Test Collections/Cran/")
    # documents = LoadIMDBDataset("./Test Collections/imdb/")
    # documents = LoadNewsgroupDataset("./Test Collections/Newsgroups/")
    boolean = BooleanModel(documents)
    return boolean
