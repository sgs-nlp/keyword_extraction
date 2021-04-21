# from nvd_plp import STOPWORDS

#
# class Extractor:
#     def __init__(self, stopwords: list = None, minimum_frequency: float = 0.12, maximum_frequency: float = 1) -> None:
#         """
#
#         :param stopwords: list paythoni az stopword ha.
#         :param minimum_frequency: adadi beyene sefr va yek,
#          kamtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
#         :param maximum_frequency: adadi beyene sefr va yek,
#          bishtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
#         """
#         if stopwords is None:
#             self.stopwords = STOPWORDS
#         self.minimum_frequency = minimum_frequency
#         self.maximum_frequency = maximum_frequency
#
#     def keywords(self, document: str, corpus: list = None) -> list:
#         """
#
#         :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
#         konim.
#         :param corpus: majmoe tamame motoni k gharar ast arzeshe kalamate document dar an corpus taein shavad.
#         :return: list pythoni shamele kalamate ba arzeshe document.
#         """
#         words_frequency_list = self._tfidf(
#             document=document,
#             corpus=corpus,
#             stopwords=self.stopwords
#         )
#         keywords_list = []
#         for (word, frequency) in words_frequency_list.items():
#             if self.minimum_frequency < frequency < self.maximum_frequency:
#                 keywords_list.append(word)
#         return keywords_list
#
#     @staticmethod
#     def _tfidf(document: str, corpus: list = None, stopwords: list = None) -> dict:
#         """
#
#         :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
#             konim.
#         :param corpus: majmoe tamame motoni k gharar ast arzeshe kalamate document dar an corpus taein shavad.
#         :param stopwords: list pythoni shsmele kamAlte stopword.
#         :return: yek dictionary pythoni bar migardanad k keyword haye an kalamate darone document ast va value an
#         barabarast ba meghdare tfidf mohasebe shude.
#         """
#         if stopwords is None:
#             stopwords = []
#         if corpus is None:
#             corpus = []
#
#         _doc = ''
#         for wrd in document.split(' '):
#             print(wrd, len(wrd))
#             if wrd not in stopwords:
#
#                 _doc = _doc + f'{wrd} '
#             else:
#                 print(wrd)
#         document = _doc
#         print(document)
#         _corpus = [document]
#         for doc in corpus:
#             _doc = ''
#             for wrd in doc.split(' '):
#                 if wrd in stopwords:
#                     continue
#                 _doc = _doc + f'{wrd} '
#             _corpus.append(_doc)
#
#         corpus = _corpus
#
#         from sklearn.feature_extraction.text import TfidfVectorizer
#         _vectorizer = TfidfVectorizer()
#         vectors = _vectorizer.fit_transform(corpus)
#         feature_names = _vectorizer.get_feature_names()
#         dense = vectors.todense()
#         dense_list = dense.tolist()
#         dense_list = dense_list[0]
#         df = {}
#         for i in range(len(feature_names)):
#             if dense_list[i] == 0:
#                 continue
#             df[feature_names[i]] = dense_list[i]
#         return df


class Stopwords:
    def __init__(self, stopwords_list: list = None):
        if stopwords_list is not None:
            self.STOPWORDSLIST = stopwords_list
        else:
            from nvd_plp import STOPWORDS
            self.STOPWORDSLIST = STOPWORDS

    def is_stopword(self, word: str) -> bool:
        if word in self.STOPWORDSLIST:
            return True
        return False


class Keywords:
    def __init__(self, stopwords_list: list = None, minimum_frequency: float = 0.5,
                 maximum_frequency: float = 1) -> None:
        """

        :param stopwords_list: list paythoni az stopword ha.
        :param minimum_frequency: adadi beyene sefr va yek,
         kamtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
        :param maximum_frequency: adadi beyene sefr va yek,
         bishtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
        """
        if stopwords_list is not None:
            self.stopwords_list = stopwords_list

        self.minimum_frequency = minimum_frequency
        self.maximum_frequency = maximum_frequency

        fry = Frequency(self.stopwords_list)
        self.frequency_func = fry.normal_tfidf

    stopwords_list = []

    def by_frequency(self, document: list, func=None) -> list:
        if func is None:
            func = self.frequency_func
        keywords = []
        res = func(document)
        for (word, value) in res.items():
            if self.minimum_frequency <= value <= self.maximum_frequency:
                keywords.append(word)
        return keywords

    # def list(self, document: str, corpus: list = None) -> list:
    #     """
    #
    #     :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
    #     konim.
    #     :param corpus: majmoe tamame motoni k gharar ast arzeshe kalamate document dar an corpus taein shavad.
    #     :return: list pythoni shamele kalamate ba arzeshe document.
    #     """
    #     words_frequency_list = tfidf(
    #         document=document,
    #         corpus=corpus,
    #         stopwords=self.stopwords_list
    #     )
    #     keywords_list = []
    #     for (word, frequency) in words_frequency_list.items():
    #         if self.minimum_frequency < frequency < self.maximum_frequency:
    #             keywords_list.append(word)
    #     return keywords_list


# def tfidf2(document: list, corpus: list, stopwords: list) -> dict:
#     """
#
#     :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
#         konim.
#     :param corpus: majmoe tamame motoni k gharar ast arzeshe kalamate document dar an corpus taein shavad.
#     :param stopwords: list pythoni shsmele kamAlte stopword.
#     :return: yek dictionary pythoni bar migardanad k keyword haye an kalamate darone document ast va value an
#     barabarast ba meghdare tfidf mohasebe shude.
#     """
#     corpus.append(document)
#
#     document_term_frequency = {}
#     for sent in document:
#         for word in sent:
#             if word not in document_term_frequency and word not in stopwords:
#                 document_term_frequency[word] = 0
#
#     sum_all_fre = 0
#     for doc in corpus:
#         for sent in doc:
#             sum_all_fre += len(sent)
#
#     for doc in corpus:
#         for sent in doc:
#             for word in sent:
#                 if word in document_term_frequency:
#                     document_term_frequency[word] += 1 / sum_all_fre
#
#     document_tfidf = {}
#     from math import log as logarithm
#     for (word, tf) in document_term_frequency.items():
#         document_tfidf[word] = tf * (logarithm(1 / tf))
#
#     (word, tfidf) = document_tfidf
#     return document_tfidf


# _doc = ''
# for wrd in document.split(' '):
#     print(wrd, len(wrd))
#     if wrd not in stopwords:
#
#         _doc = _doc + f'{wrd} '
#     else:
#         print(wrd)
# document = _doc
# print(document)
# _corpus = [document]
# for doc in corpus:
#     _doc = ''
#     for wrd in doc.split(' '):
#         if wrd in stopwords:
#             continue
#         _doc = _doc + f'{wrd} '
#     _corpus.append(_doc)
#
# corpus = _corpus
#
# from sklearn.feature_extraction.text import TfidfVectorizer
# _vectorizer = TfidfVectorizer()
# vectors = _vectorizer.fit_transform(corpus)
# feature_names = _vectorizer.get_feature_names()
# dense = vectors.todense()
# dense_list = dense.tolist()
# dense_list = dense_list[0]
# df = {}
# for i in range(len(feature_names)):
#     if dense_list[i] == 0:
#         continue
#     df[feature_names[i]] = dense_list[i]
# return df


class Frequency:
    def __init__(self, stopwords_list: list = None):
        if stopwords_list is not None:
            self._stopwords_list = stopwords_list

    _stopwords_list = []

    def tfidf(self, document: list) -> dict:
        """

        :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
            konim.

        :return: yek dictionary pythoni bar migardanad k keyword haye an kalamate darone document ast va value an
        barabarast ba meghdare tfidf mohasebe shude.
        """
        sum_all_fre = 0
        for sent in document:
            sum_all_fre += len(sent)

        document_term_frequency = {}
        for sent in document:
            for word in sent:
                if word not in self._stopwords_list:
                    if word not in document_term_frequency:
                        document_term_frequency[word] = 1 / sum_all_fre
                    else:
                        document_term_frequency[word] += 1 / sum_all_fre

        document_tfidf = {}
        from math import log as logarithm
        for (word, tf) in document_term_frequency.items():
            document_tfidf[word] = tf * (logarithm(1 / tf))

        return document_tfidf

    def normal_tfidf(self, document: list) -> dict:
        """

        :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
            konim.


        :return: yek dictionary pythoni bar migardanad k keyword haye an kalamate darone document ast va value an
        barabarast ba meghdare tfidf mohasebe shude.
        """
        document_tfidf = self.tfidf(document)

        values = document_tfidf.values()
        maximum_frequency = max(values)
        minimum_frequency = min(values)
        for (word, value) in document_tfidf.items():
            document_tfidf[word] = (value - minimum_frequency) / (maximum_frequency - minimum_frequency)

        return document_tfidf
