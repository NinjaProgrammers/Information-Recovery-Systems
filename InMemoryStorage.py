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
        return self.documentsMap