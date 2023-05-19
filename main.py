from src.hh_api import HeadHunterAPI
from src.sj_api import SuperJobApi
from src.vacancy import Vacancy
from src.json_saver import JsonSaver
from pprint import pprint


if __name__ == '__main__':
    hh = HeadHunterAPI()
    sj = SuperJobApi()

    vacancy_list_hh = hh.get_vacancies('Python Developer', 50)
    vacancy_list_sj = sj.get_vacancies('Python Developer', 50)

    json_saver = JsonSaver()

    json_saver.add_vacancy(vacancy_list_sj)
    pprint(vacancy_list_sj)


    def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
        pass

    def sort_vacancies(filtered_vacancies):
        pass

    def get_top_vacancies(sorted_vacancies, top_n):
        pass

    def user_interaction():
         platforms = ["HeadHunter", "SuperJob"]
         platform_choice = int(input("Укажите платформу для поиска: 1 - HeadHunter, 2 - SuperJob: "))
         search_query = input("Введите поисковый запрос: ")
         top_n = int(input("Введите количество вакансий для вывода в топ N: "))
         filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
    #
    # if not filtered_vacancies:
    #     print("Нет вакансий, соответствующих заданным критериям.")
    #     return
    #
    # sorted_vacancies = sort_vacancies(filtered_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)