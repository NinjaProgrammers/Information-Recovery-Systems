from InMemoryStorage import InMemoryStorage
from boolean.BooleanConsultor import BooleanConsultor
from boolean.BooleanProcessor import BooleanProcessor
from boolean.BooleanQueryProcessor import BooleanQueryProcessor
from boolean.BooleanModel import BooleanModel
from fileProcessing.FileProcessing import readDocument
from fileProcessing.cran.Parser import parseDocuments


if __name__ == "__main__":

    text = readDocument("Test Collections/Cran/cran.all.1400")
    documents = parseDocuments(text)

    terms = []
    for i in documents:
        for j in i.content.split():
            if not j in terms:
                terms.append(j)

    storage = InMemoryStorage()
    consultor = BooleanConsultor()
    processor = BooleanProcessor(terms)
    queryProcessor = BooleanQueryProcessor(terms)
    booleanModel = BooleanModel(storage, consultor, processor, queryProcessor)
