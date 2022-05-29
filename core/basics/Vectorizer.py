import numpy as np
from nltk.stem.snowball import EnglishStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from numpy import float32

class Vectorizer:
    def __init__(self, corpus, binary=False):
        _stemmer = EnglishStemmer()
        _analyzer = CountVectorizer().build_analyzer()

        self.analyzer = self.__StemmerAnalyzer__(_stemmer, _analyzer)

        if len(corpus) >= 100: self.counter = CountVectorizer(analyzer=self.analyzer, max_df=.85, binary=binary, max_features=5000)
        else: self.counter = CountVectorizer(analyzer=self.analyzer, binary=binary, max_features=5000)
        X = self.counter.fit_transform(corpus)
        self.transformer = TfidfTransformer()
        self.transformer.fit(X)

        self.N = len(corpus)
        self.vocabulary = len(self.counter.get_feature_names_out())

        X = np.where(X.toarray() > 0, 1, 0)
        self.df = np.sum(X, axis=0)

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
        return np.array(self.counter.transform(document).indices)

    def Transform(self, document):
        if isinstance(document, str):
            document = [document]
        array = self.counter.transform(document)
        array = self.transformer.transform(array).toarray()
        return array.reshape(array.size).astype(float32)

    def Features(self):
        return self.counter.get_feature_names_out()

    def Stopwords(self):
        return self.counter.stop_words_