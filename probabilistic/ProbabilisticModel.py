from basics.BasicModel import BasicModel
from basics.BasicStorage import BasicStorage
from probabilistic.ProbabilisticProcessor import ProbabilisticProcessor
from probabilistic.ProbabilisticConsultor import ProbabilisticConsultor
from probabilistic.ProbabilisticQueryProcessor import ProbabilisticQueryProcessor

class ProbabilisticModel(BasicModel):
    def __init__(self, storage: BasicStorage, terms):
        consultor = ProbabilisticConsultor()
        processor = ProbabilisticProcessor(terms)
        queryProcessor = ProbabilisticQueryProcessor(terms)
        super().__init__(storage, consultor, processor, queryProcessor)

    def Consult(self, query):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        RSV = self.processor.GetRSV()
        queryRSV = [i * j for i, j in zip(processedQuery, RSV)]
        documents = self.storage.GetAllDocuments()
        return self.consultor.Consult(documents, queryRSV)