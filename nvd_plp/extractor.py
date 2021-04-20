from nvd_plp import STOPWORDS


def _tfidf(document: str, corpus: list = None, stopwords: list = None) -> dict:
    """

    :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
        konim.
    :param corpus: majmoe tamame motoni k gharar ast arzeshe kalamate document dar an corpus taein shavad.
    :param stopwords: list pythoni shsmele kamAlte stopword.
    :return: yek dictionary pythoni bar migardanad k keyword haye an kalamate darone document ast va value an
    barabarast ba meghdare tfidf mohasebe shude.
    """
    if stopwords is None:
        stopwords = []
    if corpus is None:
        corpus = []

    _doc = ''
    for wrd in document.split(' '):
        if wrd in stopwords:
            continue
        _doc = _doc + f'{wrd} '
    document = _doc

    _corpus = [document]
    for doc in corpus:
        _doc = ''
        for wrd in doc.split(' '):
            if wrd in stopwords:
                continue
            _doc = _doc + f'{wrd} '
        _corpus.append(_doc)

    corpus = _corpus

    from sklearn.feature_extraction.text import TfidfVectorizer
    _vectorizer = TfidfVectorizer()
    vectors = _vectorizer.fit_transform(corpus)
    feature_names = _vectorizer.get_feature_names()
    dense = vectors.todense()
    dense_list = dense.tolist()
    dense_list = dense_list[0]
    df = {}
    for i in range(len(feature_names)):
        if dense_list[i] == 0:
            continue
        df[feature_names[i]] = dense_list[i]
    return df


class Extractor:
    def __init__(self, stopwords: list = None, minimum_frequency: float = 0.12, maximum_frequency: float = 1) -> None:
        """

        :param stopwords: list paythoni az stopword ha.
        :param minimum_frequency: adadi beyene sefr va yek,
         kamtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
        :param maximum_frequency: adadi beyene sefr va yek,
         bishtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
        """
        if stopwords is None:
            self.stopwords = STOPWORDS
        self.minimum_frequency = minimum_frequency
        self.maximum_frequency = maximum_frequency

    def keywords(self, document: str, corpus: list = None) -> list:
        """

        :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
        konim.
        :param corpus: majmoe tamame motoni k gharar ast arzeshe kalamate document dar an corpus taein shavad.
        :return: list pythoni shamele kalamate ba arzeshe document.
        """
        words_frequency_list = _tfidf(
            document=document,
            corpus=corpus,
            stopwords=self.stopwords
        )
        keywords_list = []
        for (word, frequency) in words_frequency_list.items():
            if self.minimum_frequency < frequency < self.maximum_frequency:
                keywords_list.append(word)
        return keywords_list
