from basics.BasicProcessor import BasicProcessor

class BooleanProcessor(BasicProcessor):
    def __init__(self, vectorizer):
        super().__init__(vectorizer)

    def ProcessDocument(self, document):
        document.tokens = self.vectorizer.BooleanTransform(str(document))
        return document.tokens.indices