from basics.BasicModel import BasicModel
from basics.BasicStorage import BasicStorage
from boolean.BooleanConsultor import BooleanConsultor
from boolean.BooleanProcessor import BooleanProcessor
from boolean.BooleanQueryProcessor import BooleanQueryProcessor
from basics.Vectorizer import Vectorizer
from basics.Document import Document

class BooleanModel(BasicModel):
    def __init__(self, storage: BasicStorage, vectorizer: Vectorizer):
        consultor = BooleanConsultor()
        processor = BooleanProcessor(vectorizer)
        queryProcessor = BooleanQueryProcessor(vectorizer)
        super().__init__(storage, vectorizer, consultor, processor, queryProcessor)

    def AddDocument(self, document: Document):
        super().AddDocument(document)

    def Consult(self, query, relaxed=None):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        documents = self.storage.GetDocumentRepresentations()
        remarkable = self.consultor.Consult(documents, [processedQuery], relaxed)
        return self.storage.GetDocuments(remarkable)