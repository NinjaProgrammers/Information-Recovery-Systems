from basics.BasicModel import BasicModel
from basics.BasicStorage import BasicStorage
from probabilistic.ProbabilisticProcessor import ProbabilisticProcessor
from probabilistic.ProbabilisticConsultor import ProbabilisticConsultor
from probabilistic.ProbabilisticQueryProcessor import ProbabilisticQueryProcessor
from math import log2

from numpy import float32

class ProbabilisticModel(BasicModel):
    def __init__(self, storage: BasicStorage, vectorizer):
        consultor = ProbabilisticConsultor()
        processor = ProbabilisticProcessor(vectorizer)
        queryProcessor = ProbabilisticQueryProcessor(vectorizer)
        super().__init__(storage, vectorizer, consultor, processor, queryProcessor)

    def Consult(self, query):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        processedQuery = processedQuery.astype(float32)
        RSV = self.GetRSV()
        for i, index in enumerate(processedQuery.indices):
            processedQuery.data[i] *= RSV[index]
        documents = self.storage.GetAllDocuments()
        return self.consultor.Consult(documents, processedQuery)

    def GetRSV(self):
        ri = [i / self.vectorizer.N for i in self.vectorizer.df]
        pi = [0.5 for _ in range(len(self.vectorizer.Features()))]
        return [log2((p * (1 - r) ) / (r * (1 - p))) for p, r in zip(pi, ri)]
