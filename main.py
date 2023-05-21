from src.hh_api import HeadHunterAPI
from src.sj_api import SuperJobApi
from src.json_saver import JsonSaver
from pprint import pprint


def user_interaction():

    platform_choice = int(input("Укажите платформу для поиска: 1 - HeadHunter, 2 - SuperJob \n"))
    filter_words = input("Введите ключевое слово для фильтрации вакансий:\n")
    pages = int(input("Какое количество страниц вы хотите просмотреть?\n"))
    filtered_by_salary = int(input("Введите минимальный порог з/п в рублях \n"))
    user_inputs = {'platform': platform_choice, 'keyword': filter_words, 'pages': pages, 'min_salary': filtered_by_salary}
    return user_inputs


def user_delete_vacancy(json_saver):

    while True:
        delete_question = input("Хотите ли вы удалить вакансию? да/нет(завершить работу программы)\n")
        if delete_question == "да".lower():
            vid = str(input("Напишите id вакансии, которую вы хотите удалить:\n"))
            json_saver.delete_vacancy(vid)
        elif delete_question == "нет".lower():
            break
        else:
            print("Неверный ввод. Ожидается ДА или НЕТ")


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

    user_delete_vacancy(json_saver)


if __name__ == '__main__':
    main()