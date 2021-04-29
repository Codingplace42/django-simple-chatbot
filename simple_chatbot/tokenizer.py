import re
import nltk
from nltk import word_tokenize
from simple_chatbot import settings

nltk.download('punkt')

if settings.DEFAULT_STEMMER:
    module_name = ".".join(settings.DEFAULT_STEMMER.split(".")[:-1])
    class_name = settings.DEFAULT_STEMMER.split(".")[-1]
    exec(f"from {module_name} import {class_name}")
    exec("STEMMER = LancasterStemmer()")
else:
    STEMMER = None


def get_tokens_from_pattern(pattern):
    tokens = []
    alphanumerical_pattern = re.sub(r'[^a-zA-Z0-9 ]', '', pattern).lower()
    words = word_tokenize(alphanumerical_pattern)
    if STEMMER:
        words = [STEMMER.stem(word) for word in words]
    tokens.extend(words)
    return list(set(tokens))
