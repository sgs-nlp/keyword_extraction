def print_hi(name):
    from nvd_plp import Extractor
    document = 'سلام من خوبم تو چطوری'
    corpus = [
        'محمد در کتابخانه ثبت نام کرده است.',
        'علی پسر خوبی است',
        'من خوب نیستم او چطوره'
        ,
    ]
    ext = Extractor()
    print(ext.keywords(document))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
