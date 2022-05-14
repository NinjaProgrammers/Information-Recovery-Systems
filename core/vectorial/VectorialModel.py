from core.vectorial.VectorialConsultor import VectorialConsultor
from core.vectorial.VectorialProcessor import VectorialProcessor
from core.basics.BasicModel import BasicModel
from core.basics.BasicStorage import BasicStorage
from core.basics.Vectorizer import Vectorizer
from core.vectorial.VectorialQueryProcessor import VectorialQueryProcessor


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