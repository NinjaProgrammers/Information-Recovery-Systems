from core.basics import BasicConsultor
from core.basics import BasicProcessor
from core.basics import BasicQueryProcessor
from core.basics import BasicStorage
from core.basics import Document
from core.basics import Vectorizer


class BasicModel:

    def __init__(self, storage: BasicStorage, vectorizer: Vectorizer,
                 consultor: BasicConsultor, processor: BasicProcessor,
                 queryProcessor: BasicQueryProcessor):
        self.storage = storage
        self.vectorizer = vectorizer
        self.consultor = consultor
        self.processor = processor
        self.queryProcessor = queryProcessor

    def AddDocument(self, document: Document):
        representation = self.processor.ProcessDocument(document)
        self.storage.SaveDocument(document, representation)

    def Consult(self, query):
        raise NotImplementedError()







