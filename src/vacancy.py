class Vacancy:
    """Класс для работы с вакансиями
    """

    def __init__(self, vid, name, url, salary_from, salary_to, currency, employer, api):
        self.vid = vid
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employer = employer
        self.api = api

    def __str__(self):
        return f"id:{self.vid}\nВакансия: {self.name}.\nРаботодатель: {self.employer}\nМинимальная з\п: {self.salary_from} {self.currency}.\nURL: {self.url}\n"

    def __repr__(self):
        return f"id:{self.vid}\nВакансия: {self.name}.\nРаботодатель: {self.employer}\nМинимальная з\п: {self.salary_from} {self.currency}.\nURL: {self.url}\n"

    def __gt__(self, other):
        return self.salary_from > other.salary_from
