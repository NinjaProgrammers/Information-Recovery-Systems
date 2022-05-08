from statistics import mean
from basics.Vectorizer import Vectorizer
from metrics.BooleanModelMetrics import MeasureBooleanModel
from fileProcessing.Loader import LoadCranDataset

if __name__ == "__main__":
    documents, consults = LoadCranDataset()

    vectorizer = Vectorizer([str(i) for i in documents])
    for i in documents: i.tokens = list(vectorizer.Analyze(str(i)))
    for i in consults: i.tokens = list(vectorizer.Analyze(str(i)))

    precission, recall = MeasureBooleanModel(documents, consults, vectorizer.Features())
    print(mean(precission), mean(recall))

