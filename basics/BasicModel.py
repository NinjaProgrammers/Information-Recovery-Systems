from basics.BasicStorage import BasicStorage
from basics.BasicProcessor import BasicProcessor
from basics.BasicConsultor import BasicConsultor
from basics.BasicQueryProcessor import BasicQueryProcessor
from basics.Document import Document
from basics.Vectorizer import Vectorizer

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






