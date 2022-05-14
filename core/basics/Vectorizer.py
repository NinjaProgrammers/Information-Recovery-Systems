from nltk.stem.snowball import EnglishStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class Vectorizer:
    def __init__(self, corpus, binary=False):
        _stemmer = EnglishStemmer()
        _analyzer = CountVectorizer().build_analyzer()

        self.analyzer = self.__StemmerAnalyzer__(_stemmer, _analyzer)

        if len(corpus) >= 100: self.counter = CountVectorizer(analyzer=self.analyzer, max_df=.85)
        else: self.counter = CountVectorizer(analyzer=self.analyzer, binary=binary)
        X = self.counter.fit_transform(corpus)
        self.transformer = TfidfTransformer()
        self.transformer.fit(X)

        self.N = len(corpus)
        self.df = [0 for _ in range(len(self.counter.get_feature_names_out()))]
        for i in X:
            for j in i.indices:
                self.df[j] += 1

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