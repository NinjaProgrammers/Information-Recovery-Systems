from basics.BasicModel import BasicModel
from basics.BasicStorage import BasicStorage
from boolean.BooleanConsultor import BooleanConsultor
from boolean.BooleanProcessor import BooleanProcessor
from boolean.BooleanQueryProcessor import BooleanQueryProcessor

class BooleanModel(BasicModel):
    def __init__(self, storage: BasicStorage, terms):
        consultor = BooleanConsultor()
        processor = BooleanProcessor(terms)
        queryProcessor = BooleanQueryProcessor(terms)
        super().__init__(storage, consultor, processor, queryProcessor)

    def Consult(self, query, relaxed=None):
        processedQuery = self.queryProcessor.ProcessQuery(query.tokens)
        documents = self.storage.GetDocumentRepresentations()
        remarkable = self.consultor.Consult(documents, [processedQuery], relaxed)
        return self.storage.GetDocuments(remarkable)