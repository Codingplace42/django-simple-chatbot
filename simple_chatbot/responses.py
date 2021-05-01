from abc import ABC, abstractmethod
from random import choice


class BaseResponse(ABC):
    @abstractmethod
    def get_response(self):
        pass


class GenericRandomResponse(BaseResponse):
    choices = ()

    def get_response(self):
        return choice(self.choices)


class GreetingResponse(GenericRandomResponse):
    choices = ("Hey I'm fine, how can I help you?",
               "Hey friend. I'm fine, hope you too! How can I help you?")


class RecomendationResponse(GenericRandomResponse):
    choices = ("Here are currently no blogs to recommend. I advice you to google.",
               "I do like Python blogs, very interesting stuff!",
               "My personal recommendation for today: Read sth. about Django!")
