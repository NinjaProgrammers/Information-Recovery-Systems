from core.boolean.BooleanProcessor import BooleanProcessor
from core.boolean.BooleanQueryProcessor import BooleanQueryProcessor
from core.boolean.BooleanConsultor import BooleanConsultor
from core.basics.Document import Document
from core.basics.BasicModel import BasicModel
from core.basics.BasicStorage import BasicStorage
from core.basics.Vectorizer import Vectorizer


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
        remarkable = self.consultor.Consult(documents, processedQuery, relaxed)
        return self.storage.GetDocuments(remarkable)