from src.vacancy_service import VacancyService


class JsonSaver(VacancyService):

    def __init__(self):
        pass

    def add_vacancy(self, vacancy):
        pass

    def filter_vacancies(self, salary):
        pass

    def delete_vacancy(self, vacancy):
        pass

    # def save_vacancies(self, text):
    #     for page in range(0, 20):
    #
    #         # Преобразуем текст ответа запроса в справочник Python
    #         js_obj = json.loads(self.get_vacancies(text, page))
    #
    #         # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
    #         # Определяем количество файлов в папке для сохранения документа с ответом запроса
    #         # Полученное значение используем для формирования имени документа
    #         nextFileName = './docs/pagination/{}.json'.format(len(os.listdir('./docs/pagination')))
    #
    #         # Создаем новый документ, записываем в него ответ запроса, после закрываем
    #         f = open(nextFileName, mode='w', encoding='utf8')
    #         f.write(json.dumps(js_obj, ensure_ascii=False))
    #         f.close()
    #
    #         # Проверка на последнюю страницу, если вакансий меньше 2000
    #         if (js_obj['pages'] - page) <= 1:
    #             break
    #
    #         # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
    #         time.sleep(0.25)
    #
    #     print('Старницы поиска собраны')