import nltk
from django.conf import settings
from django.test.signals import setting_changed

nltk.download('punkt')


DEFAULTS = {
    'STEMMER_MODULE': 'nltk.stem.lancaster.LancasterStemmer',
    "responses": ()
}

MODULES = {
    "STEMMER": None
}

IMPORT_STRINGS = [
    'stemmer',
]


class SimpleChatbotSettings:
    def __init__(self, user_settings=None, defaults=None, modules=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS
        self.modules = modules or MODULES
        self.set_stemmer()
        self._cached_attrs = set()

    def set_stemmer(self):
        module = self.user_settings.get('STEMMER_MODULE')
        if not module:
            module = self.defaults['STEMMER_MODULE']

        if module:
            module_name = ".".join(module.split(".")[:-1])
            class_name = module.split(".")[-1]
            exec(f"from {module_name} import {class_name}")
            exec(f"self.modules['STEMMER'] = {class_name}()")
        else:
            self.modules['STEMMER'] = None

    def __check_user_settings(self, user_settings):
        return user_settings

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'SIMPLE_CHATBOT', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, '_user_settings'):
            delattr(self, '_user_settings')


simple_chatbot_settings = SimpleChatbotSettings(None, DEFAULTS, MODULES)


def reload_simple_chatbot_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting == 'SIMPLE_CHATBOT':
        simple_chatbot_settings.reload()


setting_changed.connect(reload_simple_chatbot_settings)
