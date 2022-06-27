from statistics import mean

from core.fileProcessing.Loader import LoadCranDataset, LoadMedDataset
from core.basics.Vectorizer import Vectorizer
from core.metrics.BooleanModelMetrics import MeasureBooleanModel
from core.metrics.VectorialModelMetrics import MeasureVectorialModel
from core.metrics.ProbabilisticModelMetrics import MeasureProbabilisticModel

if __name__ == "__main__":
    documents, consults = LoadMedDataset("../Test Collections/Med/")

    precission, recall, time = MeasureBooleanModel(documents, consults)
    print(mean(precission), mean(recall), mean(time))
    # presicion: 0.6320939904124775 recall: 0.8667830687830688
    # 0.5173405778585659 0.8575238095238096 0.270543434354994 with relaxed=0.5

    precission, recall, mapMeasures, time = MeasureVectorialModel(documents, consults)
    print(mean(precission), mean(recall), mean(mapMeasures), mean(time))
    # precision: 0.4054624721585758 recall: 0.4054624721585758 map: 0.27770222466506916
    # 0.4660001019570855 0.4660001019570855 0.351396020904683 0.033897741105821395

    precission, recall, mapMeasures, time = MeasureProbabilisticModel(documents, consults)
    print(mean(precission), mean(recall), mean(mapMeasures), mean(time))
    # precision 0.4660001019570855 recall: 0.4660001019570855 map: 0.351396020904683
    # 0.3979382167903273 0.3979382167903273 0.22976914152516625 0.0967183060116238 without retro
    # 0.36950066841136336 0.36950066841136336 0.2095269047293856 1.7952972613440619 with retro=20
