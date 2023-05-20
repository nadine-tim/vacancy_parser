from src.hh_api import HeadHunterAPI
from src.sj_api import SuperJobApi
from src.vacancy import Vacancy
from src.json_saver import JsonSaver
from pprint import pprint


def user_interaction():

    platform_choice = int(input("Укажите платформу для поиска: 1 - HeadHunter, 2 - SuperJob \n"))
    filter_words = input("Введите ключевые слова для фильтрации вакансий:\n").split()
    pages = int(input("Какое количество страниц вы хотите просмотреть?\n"))
    filtered_by_salary = int(input("Введите минимальный порог з\п\ в рублях n"))
    user_inputs = {'platform': platform_choice, 'keyword': filter_words, 'pages': pages, 'min_salary': filtered_by_salary}
    return user_inputs


# filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
#
# if not filtered_vacancies:
#     print("Нет вакансий, соответствующих заданным критериям.")
#     return
#
# sorted_vacancies = sort_vacancies(filtered_vacancies)
# top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
# print_vacancies(top_vacancies)

def main():
    vacancies = []
    user_inputs = user_interaction()
    if user_inputs['platform'] == 1:
        hh = HeadHunterAPI()
        vacancies = hh.get_vacancies(user_inputs['keyword'], user_inputs['pages'])
    elif user_inputs['platform'] == 2:
        sj = SuperJobApi()
        vacancies = sj.get_vacancies(user_inputs['keyword'], user_inputs['pages'])

    json_saver = JsonSaver()
    json_saver.add_vacancy(vacancies)

    pprint(json_saver.filter_vacancies(user_inputs['min_salary']))


# def filter_vacancies(hh_vacancies, superjob_vacancies, filter_words):
#     pass
#
#
# def sort_vacancies(filtered_vacancies):
#     pass
#
#
# def get_top_vacancies(sorted_vacancies, top_n):
#     pass


if __name__ == '__main__':
    main()