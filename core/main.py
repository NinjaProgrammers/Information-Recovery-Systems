from statistics import mean

from core.fileProcessing.Loader import LoadCranDataset
from core.basics.Vectorizer import Vectorizer
from core.metrics.BooleanModelMetrics import MeasureBooleanModel
from core.metrics.VectorialModelMetrics import MeasureVectorialModel
from core.metrics.ProbabilisticModelMetrics import MeasureProbabilisticModel

if __name__ == "__main__":
    documents, consults = LoadCranDataset()

    vectorizer = Vectorizer([str(i) for i in documents], True)
    precission, recall = MeasureBooleanModel(documents, consults, vectorizer)
    print(mean(precission), mean(recall))
    # presicion: 0.6320939904124775 recall: 0.8667830687830688

    vectorizer = Vectorizer([str(i) for i in documents])
    precission, recall, mapMeasures = MeasureVectorialModel(documents, consults, vectorizer)
    print(mean(precission), mean(recall), mean(mapMeasures))
    #precision: 0.4054624721585758 recall: 0.4054624721585758 map: 0.27770222466506916

    vectorizer = Vectorizer([str(i) for i in documents], True)
    precission, recall, mapMeasures = MeasureProbabilisticModel(documents, consults, vectorizer)
    print(mean(precission), mean(recall), mean(mapMeasures))
    #precision 0.4660001019570855 recall: 0.4660001019570855 map: 0.351396020904683


