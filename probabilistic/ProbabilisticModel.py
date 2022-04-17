from ..basics.BasicModel import BasicModel
from ..basics.BasicStorage import BasicStorage
from .ProbabilisticProcessor import ProbabilisticProcessor
from ..basics.BasicConsultor import BasicConsultor
from ..basics.BasicQueryProcessor import BasicQueryProcessor

class ProbabilisticModel(BasicModel):
    def __init__(self, storage: BasicStorage, consultor: BasicConsultor, processor: ProbabilisticProcessor,
                 queryProcessor: BasicQueryProcessor):
        super().__init__(storage, consultor, processor, queryProcessor)

    def Consult(self, query):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        RSV = self.processor.GetRSV()
        queryRSV = [i * j for i, j in zip(processedQuery, RSV)]
        documents = self.storage.GetAllDocuments()
        return self.consultor.Consult(documents, queryRSV)