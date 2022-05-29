from core.fileProcessing.FileProcessing import ReadDocument
from core.fileProcessing.cran.Parser import ParseDocuments
from core.fileProcessing.cran.ConsultParser import ParseConsults
from core.fileProcessing.cran.RelevancyParser import ParseRelevancyList
from core.fileProcessing.imdb.IMDBParser import ParseIMDB

def LoadCranDocuments(documentsPath):
    return ReadDocument(documentsPath)

def LoadCranConsults(consultsPath):
    return ReadDocument(consultsPath)

def LoadCranRelevancyTuples(relevancyPath):
    return ReadDocument(relevancyPath)


def LoadCranDataset(basePath):
    documentsPath = basePath + "cran.all.1400"
    consultsPath = basePath + "cran.qry"
    relevancyPath = basePath + "cranqrel"

    text = LoadCranDocuments(documentsPath)
    documents = ParseDocuments(text)

    text = LoadCranConsults(consultsPath)
    consults = ParseConsults(text)

    text = LoadCranRelevancyTuples(relevancyPath)
    relevancy = ParseRelevancyList(text)

    for id, arr in enumerate(relevancy):
        consults[id].relevant = arr

    return documents, consults

def LoadIMDBDataset(path):
    path = path + "imdb.txt"
    text = ReadDocument(path)
    documents = ParseIMDB(text)
    return documents
