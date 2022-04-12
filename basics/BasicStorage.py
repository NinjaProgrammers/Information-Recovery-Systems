class BasicStorage:
    def SaveDocument(self, document, representation):
        raise NotImplementedError()

    def GetAllDocuments(self):
        raise NotImplementedError()