from src.vacancy_service import VacancyService
from src.vacancy import Vacancy
import json


class JsonSaver(VacancyService):
    """
    Класс для работы с json-файлом: добавление, фильтрация и удаление
    """
    ru_currencies = ['rub', 'rur', 'RUR', 'RUB']
    file_path = './files/vacancies.json'

    def add_vacancy(self, vacancy_list):
        file_data = []
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            try:
                file_data = json.load(file)
            except json.decoder.JSONDecodeError:
                pass
            file_data.extend(vacancy_list)
        with open(self.file_path, 'w', encoding='utf-8') as json_file:
            json.dump(file_data, json_file, indent=4, ensure_ascii=False, separators=(',', ': '))

    def filter_vacancies(self, salary=0):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
        except FileNotFoundError:
            print(f"file not found: {self.file_path}")
            return []
        list_of_vacancies = []
        for key in vacancies:
            if key['currency'] and key['currency'] in self.ru_currencies and \
                    key['salary_from'] and int(key['salary_from']) >= salary:
                vid = key['id']
                name = key['name']
                url = key['url']
                salary_from = key['salary_from']
                salary_to = key['salary_to']
                currency = key['currency']
                employer = key['employer']
                api = key['api']
                vacancy = Vacancy(vid, name, url, salary_from, salary_to, currency, employer, api)
                list_of_vacancies.append(vacancy)
        return list_of_vacancies

    def delete_vacancy(self, vid):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
        except FileNotFoundError:
            print(f"file not found: {self.file_path}")
            return
        is_found = False
        for idx, vacancy in enumerate(vacancies):
            if vacancy['id'] == vid:
                vacancies.pop(idx)
                is_found = True
        if not is_found:
            print("Нет вакансии с таким id")
            return
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
