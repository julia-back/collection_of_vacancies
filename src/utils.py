from src.vacancies import Vacancy
from config import DATA_PATH


def clear_hh_data_by_keys(data_list: list):
    list_dicts_vacancy = []
    for vacancy_dict in data_list:
        id_ = vacancy_dict.get("id")
        name = vacancy_dict.get("name")
        area = vacancy_dict.get("area").get("name")
        if vacancy_dict.get("salary") is None:
            salary_from = 0
            salary_to = 0
            currency = "RUR"
        else:
            salary_from = vacancy_dict.get("salary").get("from")
            salary_to = vacancy_dict.get("salary").get("to")
            currency = vacancy_dict.get("salary").get("currency")
        if vacancy_dict.get("address") is None:
            address = "NoAddress"
        else:
            address = vacancy_dict.get("address").get("raw")
        alternate_url = vacancy_dict.get("alternate_url")
        responsibility = vacancy_dict.get("snippet").get("responsibility")
        experience = vacancy_dict.get("experience").get("name")
        dict_vacancy = {"id_": id_, "name": name, "area": area, "salary_from": salary_from,
                        "salary_to": salary_to,"currency": currency, "address": address,
                        "alternate_url": alternate_url, "responsibility": responsibility,
                        "experience": experience}
        list_dicts_vacancy.append(dict_vacancy)
    return list_dicts_vacancy


def get_obj_vacancy_from_dicts(list_of_dict: list[dict]):
    list_of_obj = []
    for vacancy in list_of_dict:
        obj = Vacancy(**vacancy)
        list_of_obj.append(obj)
    return list_of_obj


def filter_obj_vacancy_by_currency(list_obj: list[Vacancy], currency="RUR"):
    clear_list = []
    for vacancy in list_obj:
        if vacancy.currency.upper() == currency.upper():
            clear_list.append(vacancy)
    return clear_list


def filter_obj_vacancy_by_experience(list_obj: list[Vacancy], experience: str = None):
    clear_list = []
    for vacancy in list_obj:
        if vacancy.experience.lower() == experience.lower():
            clear_list.append(vacancy)
    return clear_list
