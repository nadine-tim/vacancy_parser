from src.vacancy_service import VacancyService
from src.vacancy import Vacancy
import json


class JsonSaver(VacancyService):

    ru_currencies = ['rub', 'rur']

    def add_vacancy(self, vacancy_list):
        with open('./files/vacancies.json', 'r+', encoding='utf-8') as file:
            json.dump(vacancy_list, file, ensure_ascii=False, indent=4)

    def filter_vacancies(self, salary=0):
        with open('./files/vacancies.json', 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            list_of_vacancies = []
            for key in vacancies:
                if key['currency'] and key['currency'] in self.ru_currencies\
                        and key['salary_from']  and int(key['salary_from']) >= salary:
                    name = key['name']
                    url = key['url']
                    salary_from = key['salary_from']
                    salary_to = key['salary_to']
                    currency = key['currency']
                    api = key['api']
                    vacancy = Vacancy(name, url, salary_from, salary_to, currency, api)
                    list_of_vacancies.append(vacancy)
            return list_of_vacancies


    def delete_vacancy(self, vacancy):
        pass
