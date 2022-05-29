from core.fileProcessing.FileProcessing import ReadDocument
from core.fileProcessing.cran.Parser import ParseDocuments
from core.fileProcessing.cran.ConsultParser import ParseConsults
from core.fileProcessing.cran.RelevancyParser import ParseRelevancyList
from core.fileProcessing.imdb.IMDBParser import ParseIMDB
from core.basics.Document import Document
from pathlib import Path

def LoadCranDocuments(documentsPath):
    return ReadDocument(documentsPath)

def LoadCranConsults(consultsPath):
    return ReadDocument(consultsPath)

def LoadCranRelevancyTuples(relevancyPath):
    return ReadDocument(relevancyPath)


def LoadCranDataset(basePath:str):
    base = Path(basePath)
    documentsPath = base / "cran.all.1400"
    consultsPath = base / "cran.qry"
    relevancyPath = base / "cranqrel"

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
    path = Path(path) / "imdb.txt"
    text = ReadDocument(path)
    documents = ParseIMDB(text)
    return documents

def LoadNewsgroupDataset(path):
    path = Path(path)
    id = 1
    documents = []
    for childPath in path.iterdir():
        for file in childPath.iterdir():
            try:
                documents.append(Document(id, file.read_text("utf8")))
                id += 1
            except:
                pass
    return documents



