def txtfiles2pylist(mypath: str) -> list:
    """
    in tabe masiri ra daryaft mikonad va tamame file haye .txt daron an directory ra khaande va dar ghalebe ye liste
    pythoni erae midahad.
    :param mypath: masire gharar gereftane file haye txt
    :return: liste pythoni shamele maghadire darone file ha
    """

    import glob
    filenames = glob.glob(f'{mypath}/*.txt')
    res = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
        res.append(data)
    return res
