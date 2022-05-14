from core import BooleanProcessor
from core import BooleanQueryProcessor
from core.basics import BasicModel
from core.basics import BasicStorage
from core.basics import Document
from core.basics import Vectorizer
from core.boolean.BooleanConsultor import BooleanConsultor


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