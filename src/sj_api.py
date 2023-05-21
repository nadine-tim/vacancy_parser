import requests
import os
from src.abstract_api import AbstractApi


class SuperJobApi(AbstractApi):
    """
    Класс обрабатывает вакансии с sj.ru
    """
    url: str = 'https://api.superjob.ru/2.0/vacancies/'
    header = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}

    def get_vacancies(self, text, page=1):
        """
        Возвращает список вакансий
        """
        vacancy_list = []

        pages_number = 0
        while pages_number < page:

            params = {
                'keyword': text,  # Текст фильтра. В имени должно быть слово "Аналитик"
                'page': pages_number,  # Индекс страницы поиска на SJ
                'count': 100  # Кол-во вакансий на 1 странице
            }

            sj_request = {}
            try:
                sj_request = requests.get(self.url, params=params, headers=self.header)  # Посылаем запрос к API
            except requests.HTTPError:
                print("bad response from superjob.ru")

            if sj_request is None:
                return []
            else:
                sj_vacancies = sj_request.json()['objects']

            for vacancy in sj_vacancies:
                vacancy_list.append({
                    'id': vacancy['id'],
                    'name': vacancy['profession'],
                    'url': vacancy['link'],
                    'experience': vacancy['experience']['title'],
                    'salary_from': vacancy['payment_from'],
                    'salary_to': vacancy['payment_to'],
                    'currency': vacancy['currency'],
                    'employer': vacancy['firm_name'],
                    'api': 'Superjob'
                })
            pages_number += 1
            print(f'Поиск на superjob.ru , номер страницы: {pages_number}')
        print(f'найдено вакансий: {len(vacancy_list)}')
        return vacancy_list

    @staticmethod
    def get_salary(salary):
        """
        Проверка наличия указания з/п вилки
        """
        salary_gross = [None, None]
        if salary and salary['from'] and salary['from'] != 0:
            salary_gross[0] = salary['from']
        if salary and salary['to'] and salary['to'] != 0:
            salary_gross[1] = salary['to']
        return salary_gross
