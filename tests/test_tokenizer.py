import pytest
from simple_chatbot import tokenizer, settings
from nltk.stem.lancaster import LancasterStemmer


@pytest.fixture
def settings_():
    return {
        "MODULES": {
            "STEMMER": LancasterStemmer()
        }
    }


class TestTokenizer:
    def test_get_tokens_from_pattern_with_stemmer(self, settings_):
        settings.MODULES = settings_["MODULES"]
        pattern = "Hello world from Chatbot! Let's have some fun ... "
        expected_tokens = ['hello', 'world', 'from', 'chatbot', 'let', 'hav', 'som', 'fun']
        tokens = tokenizer.get_tokens_from_pattern(pattern)
        assert len(expected_tokens) == len(tokens)
        assert all([a == b for a, b in zip(expected_tokens, tokens)])

    def test_get_tokens_from_pattern_without_stemmer(self):
        settings.MODULES["STEMMER"] = None
        pattern = "Hello world from Chatbot! Let's have some fun ... "
        expected_tokens = ['hello', 'world', 'from', 'chatbot', 'lets', 'have', 'some', 'fun']
        tokens = tokenizer.get_tokens_from_pattern(pattern)
        assert len(expected_tokens) == len(tokens)
        assert all([a == b for a, b in zip(expected_tokens, tokens)])
