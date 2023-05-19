import math

import requests

from src.abstract_api import AbstractApi


class HeadHunterAPI(AbstractApi):
    """
    Класс обрабатывает вакансии с hh.ru
    """
    url: str = 'https://api.hh.ru/'

    def get_vacancies(self, text, top, page=0):
        """
        Возвращает список вакансий
        """
        if top > 100:
            per_page = 100
            page = math.ceil(top / per_page)
        else:
            per_page = top

        params = {
            'text': text,  # Текст фильтра. В имени должно быть слово "Аналитик"
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': per_page  # Кол-во вакансий на 1 странице
        }

        hh_request = requests.get(self.url + 'vacancies', params).json()  # Посылаем запрос к API
        hh_vacancies = hh_request['items']
        vacancy_list = []

        for vacancy in hh_vacancies:
            salary_from, salary_to, currency = self.get_salary(vacancy['salary'])
            vacancy_list.append({
                'name': vacancy['name'],
                'url': vacancy['alternate_url'],
                'experience': vacancy['experience'],
                'salary_from': salary_from,
                'salary_to': salary_to,
                'currency': currency,
                'employer': vacancy['employer']['name'],
                'api': 'Headhunter'
            })
        return vacancy_list

    @staticmethod
    def get_salary(salary):
        salary_gross = [None, None, None]
        if salary and salary['from'] and salary['from'] != 0:
            salary_gross[0] = salary['from']
        if salary and salary['to'] and salary['to'] != 0:
            salary_gross[1] = salary['to']
        if salary and salary['currency']:
            salary_gross[2] = salary['currency']
        return salary_gross
