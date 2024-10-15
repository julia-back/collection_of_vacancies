from src.hh_api import SearchVacanciesHH
from src.vacancies import Vacancy
from config import DATA_PATH
from src.utils import (clear_hh_data_by_keys, get_obj_vacancy_from_dicts,
                       filter_obj_vacancy_by_currency, filter_obj_vacancy_by_experience)
from src.file_worker import AppenderInJSON, ReaderJSON
import os
import json


def main():
    user_input = input("Введите ключевые слова для поиска вакансий через пробел\n")
    print("Готовим для Вас вакансии...")
    vacancies = SearchVacanciesHH(user_input).get_vacancies()
    vacancies = clear_hh_data_by_keys(vacancies)
    file_appender = AppenderInJSON()
    file_appender.clear_file()
    file_appender.append_in_file(vacancies)

    file_reader = ReaderJSON()
    vacancies = file_reader.read_file()
    get_obj_vacancy_from_dicts(vacancies)
    vacancies = Vacancy.vacancies

    user_input = input("Отфильтровать по опыту? (да/нет)\n")
    if user_input.lower() == "да":
        user_input = input("Введите опыт для фильтрации:\n"
                           "0 - Нет опыта\n"
                           "1 - От 1 года до 3 лет\n"
                           "3 - От 3 до 6 лет\n"
                           "6 - Более 6 лет\n")
        if int(user_input) == 0:
            vacancies = filter_obj_vacancy_by_experience(vacancies, "Нет опыта")
        if int(user_input) == 1:
            vacancies = filter_obj_vacancy_by_experience(vacancies, "От 1 года до 3 лет")
        if int(user_input) == 3:
            vacancies = filter_obj_vacancy_by_experience(vacancies, "От 3 до 6 лет")
        if int(user_input) == 6:
            vacancies = filter_obj_vacancy_by_experience(vacancies, "Более 6 лет")

    user_input = input("Фильтровать по валюте? да/нет\n")
    if user_input.lower() == "да":
        user_input = input("Введите валюту для фильтрации (RUR, KZT, USD, BYR...)\n")
        vacancies = filter_obj_vacancy_by_currency(vacancies, user_input)

    user_input = input("Введите количество вакансий для вывода в топ по зарплате\n")
    vacancies = sorted(vacancies, key=lambda x: (x.salary_to, x.salary_from), reverse=True)
    for i in range(int(user_input)):
        print(vacancies[i])

    user_input = input("Просмотреть все вакансии? да/нет\n")
    if user_input.lower() == "да":
        for vacancy in vacancies:
            print(vacancy)


if __name__ == "__main__":
    main()
