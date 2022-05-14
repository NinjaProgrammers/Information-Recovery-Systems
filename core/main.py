from statistics import mean

from core import LoadCranDataset
from core.basics import Vectorizer
from core.metrics import MeasureProbabilisticModel

if __name__ == "__main__":
    documents, consults = LoadCranDataset()

    # vectorizer = Vectorizer([str(i) for i in documents], True)
    # precission, recall = MeasureBooleanModel(documents, consults, vectorizer)
    # print(mean(precission), mean(recall))

    # vectorizer = Vectorizer([str(i) for i in documents])
    # precission, recall, mapMeasures = MeasureVectorialModel(documents, consults, vectorizer)
    # print(mean(precission), mean(recall), mean(mapMeasures))

    vectorizer = Vectorizer([str(i) for i in documents], True)
    precission, recall, mapMeasures = MeasureProbabilisticModel(documents, consults, vectorizer)
    print(mean(precission), mean(recall), mean(mapMeasures))


