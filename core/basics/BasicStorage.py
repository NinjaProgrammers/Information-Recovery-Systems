class BasicStorage:
    def SaveDocument(self, document, representation):
        raise NotImplementedError()

    def GetAllDocuments(self):
        raise NotImplementedError()

    def GetDocuments(self, representations):
        raise NotImplementedError()

    def GetDocumentRepresentations(self):
        raise NotImplementedError()