from core.basics.BasicStorage import BasicStorage


class InMemoryStorage(BasicStorage):
    def __init__(self):
        self.documentsMap = {}
        self.representations = []
        self.documents = []

    def SaveDocument(self, document, representation):
        hashable = str(representation)
        try:
            self.documentsMap[hashable].append(len(self.documents))
        except:
            self.documentsMap[hashable] = [len(self.documents)]
            self.representations.append(representation)
        self.documents.append(document)

    def GetAllDocuments(self):
        return self.documents

    def GetDocuments(self, representations):
        documents = []
        for r in representations:
            documents.extend((self.documents[i] for i in self.documentsMap[str(r)]))
        return documents

    def GetDocumentRepresentations(self):
        return self.representations