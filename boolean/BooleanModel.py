from basics.BasicModel import BasicModel
from basics.BasicStorage import BasicStorage
from basics.BasicProcessor import BasicProcessor
from basics.BasicConsultor import BasicConsultor
from basics.BasicQueryProcessor import BasicQueryProcessor

class BooleanModel(BasicModel):
    def __init__(self, storage: BasicStorage, consultor: BasicConsultor, processor: BasicProcessor,
                 queryProcessor: BasicQueryProcessor):
        super().__init__(storage, consultor, processor, queryProcessor)

    def Consult(self, query):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        documents = self.storage.GetAllDocuments()
        return self.consultor.Consult(documents, processedQuery)