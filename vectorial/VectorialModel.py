from basics.BasicModel import BasicModel
from basics.BasicStorage import BasicStorage
from vectorial.VectorialConsultor import VectorialConsultor
from vectorial.VectorialProcessor import VectorialProcessor
from vectorial.VectorialQueryProcessor import VectorialQueryProcessor

class VectorialModel(BasicModel):
    def __init__(self, storage: BasicStorage, terms):
        consultor = VectorialConsultor()
        processor = VectorialProcessor(terms)
        queryProcessor = VectorialQueryProcessor(terms)
        super().__init__(storage, consultor, processor, queryProcessor)

    def Consult(self, query, size=1):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        documents = self.storage.GetAllDocuments()
        return self.consultor.Consult(documents, processedQuery)[:size]