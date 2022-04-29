from basics.BasicStorage import BasicStorage
from basics.BasicProcessor import BasicProcessor
from basics.BasicConsultor import BasicConsultor
from basics.BasicQueryProcessor import BasicQueryProcessor

class BasicModel:

    def __init__(self, storage: BasicStorage, consultor: BasicConsultor, processor: BasicProcessor,
                 queryProcessor: BasicQueryProcessor):
        self.storage = storage
        self.consultor = consultor
        self.processor = processor
        self.queryProcessor = queryProcessor

    def AddDocument(self, document):
        representation = self.processor.ProcessDocument(document)
        self.storage.SaveDocument(document, representation)

    def Consult(self, query):
        raise NotImplementedError()







