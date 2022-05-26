from core.basics.BasicStorage import BasicStorage
from numpy import array_equal


class InMemoryStorage(BasicStorage):
    def __init__(self):
        self.documents = []

    def SaveDocument(self, document, representation):
        self.documents.append(document)

    def GetAllDocuments(self):
        return self.documents

    def GetDocuments(self, representations):
        documents = []
        for doc in documents:
            if any(r for r in representations if array_equal(doc.tokens, r)):
                documents.append(doc)
        return documents

    def GetDocumentRepresentations(self):
        return (d.tokens for d in self.documents)