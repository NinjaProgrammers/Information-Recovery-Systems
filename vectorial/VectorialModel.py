from basics.BasicModel import BasicModel
from basics.BasicStorage import BasicStorage
from basics.Vectorizer import Vectorizer
from vectorial.VectorialConsultor import VectorialConsultor
from vectorial.VectorialProcessor import VectorialProcessor
from vectorial.VectorialQueryProcessor import VectorialQueryProcessor

class VectorialModel(BasicModel):
    def __init__(self, storage: BasicStorage, vectorizer: Vectorizer):
        consultor = VectorialConsultor()
        processor = VectorialProcessor(vectorizer)
        queryProcessor = VectorialQueryProcessor(vectorizer)
        super().__init__(storage, vectorizer, consultor, processor, queryProcessor)

    def Consult(self, query, size=None):
        processedQuery = self.queryProcessor.ProcessQuery(query)
        documents = self.storage.GetAllDocuments()
        relevant = self.consultor.Consult(documents, processedQuery)
        if size is None or size >= len(relevant): return relevant
        else: return relevant[: size]