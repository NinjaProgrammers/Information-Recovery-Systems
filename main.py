from statistics import mean
from basics.Vectorizer import Vectorizer
from fileProcessing.Loader import LoadCranDataset
from metrics.BooleanModelMetrics import MeasureBooleanModel
from metrics.VectorialModelMetrics import MeasureVectorialModel

if __name__ == "__main__":
    documents, consults = LoadCranDataset()

    vectorizer = Vectorizer([str(i) for i in documents])

    # precission, recall = MeasureBooleanModel(documents, consults, vectorizer)
    precission, recall, mapMeasures = MeasureVectorialModel(documents, consults, vectorizer)
    print(mean(precission), mean(recall), mean(mapMeasures))

