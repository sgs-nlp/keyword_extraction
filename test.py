def keyword_extraction_test():
    from nvd_plp.loader import txtfiles2pylist
    from nvd_plp.persian_pre_processing import TripleP
    from nvd_plp.extractor import Stopwords
    from nvd_plp import Keywords

    my_document_path = './.files'
    document = txtfiles2pylist(my_document_path)

    print('document:\n')
    print(document)
    print('**************')

    ppp = TripleP()
    document = ppp.tokens(document)

    sword = Stopwords()

    kwrd = Keywords(stopwords_list=sword.STOPWORDSLIST)
    keywords_list = kwrd.by_frequency(document)
    print('keywords list:\n')
    print(keywords_list)
    print('**************')
