from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.snowball import EnglishStemmer

class Vectorizer:
    def __init__(self, corpus):
        stemmer = EnglishStemmer()
        analyzer = CountVectorizer().build_analyzer()
        def stemmedWords(doc): return (stemmer.stem(w) for w in analyzer(doc))

        self.counter = CountVectorizer(analyzer=stemmedWords, max_df=.85)
        X = self.counter.fit_transform(corpus)
        self.transformer = TfidfTransformer()
        self.transformer.fit(X)

    def __call__(self, document):
        return self.transform(document)

    def countTransform(self, document):
        if isinstance(document, str):
            document = [document]
        return self.counter.transform(document)

    def transform(self, document):
        if isinstance(document, str):
            document = [document]
        a = self.counter.transform(document)
        return self.transformer.transform(a)

    def features(self):
        return self.counter.get_feature_names_out()

    def stopwords(self):
        return self.counter.stop_words_



def readDocument(address):
    f = open(address, "r")
    content = f.read()
    f.close()
    return content
