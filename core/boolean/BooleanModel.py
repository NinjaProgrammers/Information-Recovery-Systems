from core.boolean.BooleanProcessor import BooleanProcessor
from core.boolean.BooleanQueryProcessor import BooleanQueryProcessor
from core.boolean.BooleanConsultor import BooleanConsultor
from core.basics.Document import Document
from core.basics.BasicModel import BasicModel
from core.basics.BasicStorage import BasicStorage
from core.basics.Vectorizer import Vectorizer
from core.InMemoryStorage import InMemoryStorage


class BooleanModel(BasicModel):
    def __init__(self, documents, storage: BasicStorage=None, vectorizer: Vectorizer=None):
        if storage is None: storage = InMemoryStorage()
        if vectorizer is None: vectorizer = Vectorizer([str(i) for i in documents], True)
        consultor = BooleanConsultor()
        processor = BooleanProcessor(vectorizer)
        queryProcessor = BooleanQueryProcessor(vectorizer)
        super().__init__(documents, storage, vectorizer, consultor, processor, queryProcessor)

    def AddDocument(self, document: Document):
        super().AddDocument(document)

    def Consult(self, query, size=None, relaxed=None):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        if len(processedQuery) == 0:
            return []
        documents = self.storage.GetAllDocuments()
        relevant = self.consultor.Consult(documents, processedQuery, relaxed)
        if size is None or size >= len(relevant): return relevant
        else: return relevant[: size]