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

    def ReConsult(self, query, relevant=None, irrelevant=None, size=None):
        '''
        :param query: Consult object
        :param relevant: array of ints (indices of documents)
        :param irrelevant: array of ints (indices of documents)
        :param size: int
        :return: relevant documents
        '''
        processedQuery = self.queryProcessor.ProcessQuery(query)
        documents = self.storage.GetAllDocuments()
        if relevant is None or irrelevant is None:
            return self.consultor.ReConsult(documents, processedQuery)

        relevant = [d.tokens for d in documents if d.id in relevant]
        irrelevant = [d.tokens for d in documents if d.id in irrelevant]
        remarkable = self.consultor.ReConsult(documents, processedQuery, relevant, irrelevant)
        if size is None or size >= len(remarkable):
            return remarkable
        else:
            return remarkable[: size]