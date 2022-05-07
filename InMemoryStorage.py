from basics.BasicStorage import BasicStorage

class InMemoryStorage(BasicStorage):
    def __init__(self):
        self.documentsMap = {}

    def SaveDocument(self, document, representation):
        try:
            self.documentsMap[representation].append(document)
        except:
            self.documentsMap[representation] = [document]

    def GetAllDocuments(self):
        return self.documentsMap.values()

    def GetDocuments(self, representations):
        documents = []
        for r in representations:
            documents.extend(self.documentsMap[r])
        return documents

    def GetDocumentRepresentations(self):
        return list(self.documentsMap.keys())