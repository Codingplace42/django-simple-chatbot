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
