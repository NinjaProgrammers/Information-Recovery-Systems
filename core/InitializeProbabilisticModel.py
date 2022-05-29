from core.InMemoryStorage import InMemoryStorage
from core.basics.Vectorizer import Vectorizer
from core.fileProcessing.Loader import LoadCranDataset, LoadIMDBDataset, LoadNewsgroupDataset
from core.probabilistic.ProbabilisticModel import ProbabilisticModel


def InitializeProbabilisticModel():
    documents, _ = LoadCranDataset("./Test Collections/Cran/")
    # documents = LoadIMDBDataset("./Test Collections/imdb/")
    # documents = LoadNewsgroupDataset("./Test Collections/Newsgroups/")
    probabilistic = ProbabilisticModel(documents)
    return probabilistic
