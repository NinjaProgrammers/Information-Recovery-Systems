from core.fileProcessing.FileProcessing import ReadDocument
from core.fileProcessing.cran.Parser import ParseDocuments
from core.fileProcessing.cran.ConsultParser import ParseConsults
from core.fileProcessing.cran.RelevancyParser import ParseRelevancyList

path = "./Test Collections/Cran/"
documentsPath = path + "cran.all.1400"
consultsPath = path + "cran.qry"
relevancyPath = path + "cranqrel"

def LoadCranDocuments():
    return ReadDocument(documentsPath)

def LoadCranConsults():
    return ReadDocument(consultsPath)

def LoadCranRelevancyTuples():
    return ReadDocument(relevancyPath)


def LoadCranDataset():
    text = LoadCranDocuments()
    documents = ParseDocuments(text)

    text = LoadCranConsults()
    consults = ParseConsults(text)

    text = LoadCranRelevancyTuples()
    relevancy = ParseRelevancyList(text)

    for id, arr in enumerate(relevancy):
        consults[id].relevant = arr

    return documents, consults
