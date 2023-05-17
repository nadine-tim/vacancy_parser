from abc import ABC

from src.abstract_api import AbstractApi


class SuperJobApi(AbstractApi, ABC):
    """
    Класс обрабатывает вакансии с hh.ru
    """
    url: str = 'https://api.hh.ru/'

    @classmethod
    def get_vacancy(cls, text, page = 0):
        """
        Возвращает список вакансий
        """

