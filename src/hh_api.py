import requests
import json
import time
import os

from src.abstract_api import AbstractApi


class HeadHunterAPI(AbstractApi):
    """
    Класс обрабатывает вакансии с hh.ru
    """
    url: str = 'https://api.hh.ru/'

    @classmethod
    def get_vacancies(cls, text, page=0):
        """
        Возвращает список вакансий
        """
        params = {
            'text': text,  # Текст фильтра. В имени должно быть слово "Аналитик"
            # 'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 2  # Кол-во вакансий на 1 странице
        }

        req = requests.get(cls.url + 'vacancies', params).json()  # Посылаем запрос к API
        # data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        # req.close()
        return req

