from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.snowball import EnglishStemmer

class Vectorizer:
    def __init__(self, corpus):
        _stemmer = EnglishStemmer()
        _analyzer = CountVectorizer().build_analyzer()

        self.analyzer = self.__StemmerAnalyzer__(_stemmer, _analyzer)

        if len(corpus) >= 100: self.counter = CountVectorizer(analyzer=self.analyzer, max_df=.85)
        else: self.counter = CountVectorizer(analyzer=self.analyzer)
        X = self.counter.fit_transform(corpus)
        self.transformer = TfidfTransformer()
        self.transformer.fit(X)

    def __StemmerAnalyzer__(self, stemmer, analyzer):
        def stemmedWords(doc): return (stemmer.stem(w) for w in analyzer(doc))
        return stemmedWords

    def __call__(self, document):
        return self.Transform(document)

    def Analyze(self, document):
        return self.analyzer(document)

    def CountTransform(self, document):
        if isinstance(document, str):
            document = [document]
        return self.counter.transform(document)

    def Transform(self, document):
        if isinstance(document, str):
            document = [document]
        a = self.counter.transform(document)
        return self.transformer.transform(a)

    def Features(self):
        return self.counter.get_feature_names_out()

    def Stopwords(self):
        return self.counter.stop_words_



def ReadDocument(address):
    f = open(address, "r")
    content = f.read()
    f.close()
    return content
