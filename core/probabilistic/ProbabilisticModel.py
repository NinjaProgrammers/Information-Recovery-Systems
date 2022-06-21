from math import log2
import numpy as np

from core.probabilistic.ProbabilisticProcessor import ProbabilisticProcessor
from core.probabilistic.ProbabilisticQueryProcessor import ProbabilisticQueryProcessor
from core.basics.BasicModel import BasicModel
from core.basics.BasicStorage import BasicStorage
from core.probabilistic.ProbabilisticConsultor import ProbabilisticConsultor
from core.basics.Vectorizer import Vectorizer
from core.InMemoryStorage import InMemoryStorage


class ProbabilisticModel(BasicModel):
    def __init__(self, documents, storage: BasicStorage=None, vectorizer: Vectorizer=None):
        if storage is None: storage = InMemoryStorage()
        if vectorizer is None: vectorizer = Vectorizer([str(i) for i in documents], True)
        consultor = ProbabilisticConsultor(vectorizer.df, vectorizer.N)
        processor = ProbabilisticProcessor(vectorizer)
        queryProcessor = ProbabilisticQueryProcessor(vectorizer)
        super().__init__(documents, storage, vectorizer, consultor, processor, queryProcessor)
        self.eps = 1e-18

    def Consult(self, query, size=None, retroalimentation=None):
        assert(retroalimentation is None or (isinstance(retroalimentation, int) and isinstance(size, int)))
        processedQuery = self.queryProcessor.ProcessQuery(query)
        if len(processedQuery) == 0: return []
        documents = self.storage.GetAllDocuments()
        relevant = self.consultor.Consult(documents, processedQuery, size, retroalimentation)

        if size is None or size >= len(relevant): return relevant
        else: return relevant[: size]



