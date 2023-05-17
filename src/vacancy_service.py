from abc import ABC, abstractmethod


class VacancyService(ABC):

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def filter_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass
