import re
from nltk import word_tokenize
from . import settings


def get_tokens_from_pattern(pattern):
    tokens = []
    alphanumerical_pattern = re.sub(r'[^a-zA-Z0-9 ]', '', pattern).lower()
    words = word_tokenize(alphanumerical_pattern)
    if settings.MODULES["STEMMER"]:
        words = [settings.MODULES["STEMMER"].stem(word) for word in words]
    tokens.extend(words)
    return tokens
