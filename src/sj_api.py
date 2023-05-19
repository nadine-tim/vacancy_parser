import requests
import os

from src.abstract_api import AbstractApi


class SuperJobApi(AbstractApi):
    """
    Класс обрабатывает вакансии с hh.ru
    """
    url: str = 'https://api.superjob.ru/2.0/vacancies/'
    header = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}

    def get_vacancies(self, text, top, page=0):
        """
        Возвращает список вакансий
        """
        params = {
            'keyword': text,  # Текст фильтра. В имени должно быть слово "Аналитик"
            'page': 0,  # Индекс страницы поиска на HH
            'count': 100  # Кол-во вакансий на 1 странице
        }

        sj_request = requests.get(self.url, params, headers=self.header)  # Посылаем запрос к API

        sj_vacancies = sj_request.json()['objects']
        vacancy_list = []
        print(sj_vacancies)
        for vacancy in sj_vacancies:
            vacancy_list.append({
                'name': vacancy['profession'],
                'url': vacancy['link'],
                'experience': vacancy['experience']['title'],
                'salary_from': vacancy['payment_from'],
                'salary_to': vacancy['payment_to'],
                'currency': vacancy['currency'],
                'employer': vacancy['firm_name'],
                'api': 'Superjob'
            })
        return vacancy_list

    @staticmethod
    def get_salary(salary):
        salary_gross = [None, None]
        if salary and salary['from'] and salary['from'] != 0:
            salary_gross[0] = salary['from']
        if salary and salary['to'] and salary['to'] != 0:
            salary_gross[1] = salary['to']
        return salary_gross




