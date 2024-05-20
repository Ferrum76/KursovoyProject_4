from abc import ABC, abstractmethod


class AbstractHH(ABC):
    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        raise NotImplementedError


class Saver(ABC):
    @abstractmethod
    def save(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError
    

class Parser(ABC):
    @abstractmethod
    def get_vacancys(self, *args, **kwargs):
        raise NotImplementedError