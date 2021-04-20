from .extractor import Extractor
from os.path import join, dirname

BASE_DIR = dirname(__file__)
RESOURCES_URL = join(BASE_DIR, 'resources')
STOPWORDS_FILE_NAME = 'persian.stopword.json'

with open(join(RESOURCES_URL, STOPWORDS_FILE_NAME), 'r', encoding='utf-8') as file:
    from json import loads

    tmp = file.read()
    STOPWORDS = loads(tmp)