from core.basics.BasicConsultor import BasicConsultor
from core.basics.BasicQueryProcessor import BasicQueryProcessor
from core.basics.BasicStorage import BasicStorage
from core.basics.Vectorizer import Vectorizer
from core.basics.BasicProcessor import BasicProcessor
from core.basics.Document import Document


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







