from src.utils import (clear_hh_data_by_keys, filter_obj_vacancy_by_currency, filter_obj_vacancy_by_experience,
                       get_obj_vacancy_from_dicts)


def test_clear_hh_data_by_keys(vacancies_hh):
    assert clear_hh_data_by_keys(vacancies_hh) != vacancies_hh
    assert clear_hh_data_by_keys(vacancies_hh) == [
        {
            "address": "NoAddress",
            "alternate_url": "https://hh.ru/vacancy/108001774",
            "area": "Москва",
            "currency": "RUR",
            "experience": "Нет опыта",
            "id_": "108001774",
            "name": "Junior Python разработчик",
            "responsibility": "Разработка и поддержка backend части приложения на "
            "<highlighttext>Python</highlighttext>. Работа с базами "
            "данных (например, PostgreSQL, MongoDB). Написание "
            "чистого, эффективного и хорошо...",
            "salary_from": 125000,
            "salary_to": None,
        },
        {
            "address": "NoAddress",
            "alternate_url": "https://hh.ru/vacancy/108291622",
            "area": "Гомель",
            "currency": "USD",
            "experience": "Нет опыта",
            "id_": "108291622",
            "name": "Программист - разработчик Junior - .NET C# ASP Java",
            "responsibility": "Выполнение заданий разнообразного характера (структуры "
            "данных и алгоритмы, базовый CRUD, клиент-серверные "
            "приложения, работа с СУБД, веб-приложения). ",
            "salary_from": 150,
            "salary_to": 600,
        },
        {
            "address": "Санкт-Петербург, Мебельная улица, 12к2",
            "alternate_url": "https://hh.ru/vacancy/108423996",
            "area": "Санкт-Петербург",
            "currency": "RUR",
            "experience": "Нет опыта",
            "id_": "108423996",
            "name": "Программист (Junior - младший разработчик)",
            "responsibility": "Участие в интересных проектах. Доработка и разработка "
            "программного комплекса. Дополнительно: Тестирование "
            "информационных систем. Настройка информационной системы "
            "(ИС) автоматизации бизнес-процессов. ",
            "salary_from": 0,
            "salary_to": 0,
        },
    ]


def test_get_obj_vacancy_from_dicts(vacancies_dicts_by_keys):
    vacancies_obj = get_obj_vacancy_from_dicts(vacancies_dicts_by_keys)
    assert vacancies_obj[0].id_ == "108001774"
    assert vacancies_obj[0].name == "Junior Python разработчик"
    assert vacancies_obj[0].area == "Москва"
    assert vacancies_obj[0].salary_from == 125000
    assert vacancies_obj[0].salary_to == 0
    assert vacancies_obj[0].currency == "RUR"
    assert vacancies_obj[0].address == "NoAddress"
    assert vacancies_obj[0].alternate_url == "https://hh.ru/vacancy/108001774"
    assert vacancies_obj[0].responsibility == (
        "Разработка и поддержка backend части приложения на "
        "Python. Работа с базами данных (например, "
        "PostgreSQL, MongoDB). Написание чистого, эффективного и хорошо..."
    )
    assert vacancies_obj[0].experience == "Нет опыта"

    assert vacancies_obj[1].id_ == "108291622"
    assert vacancies_obj[1].name == "Программист - разработчик Junior - .NET C# ASP Java"
    assert vacancies_obj[1].area == "Гомель"
    assert vacancies_obj[1].salary_from == 150
    assert vacancies_obj[1].salary_to == 600
    assert vacancies_obj[1].currency == "USD"
    assert vacancies_obj[1].address == "NoAddress"
    assert vacancies_obj[1].alternate_url == "https://hh.ru/vacancy/108291622"
    assert vacancies_obj[1].responsibility == (
        "Выполнение заданий разнообразного характера (структуры данных и алгоритмы, "
        "базовый CRUD, клиент-серверные приложения, работа с СУБД, веб-приложения). "
    )
    assert vacancies_obj[1].experience == "Нет опыта"

    assert vacancies_obj[2].id_ == "108423996"
    assert vacancies_obj[2].name == "Программист (Junior - младший разработчик)"
    assert vacancies_obj[2].area == "Санкт-Петербург"
    assert vacancies_obj[2].salary_from == 0
    assert vacancies_obj[2].salary_to == 0
    assert vacancies_obj[2].currency == "RUR"
    assert vacancies_obj[2].address == "Санкт-Петербург, Мебельная улица, 12к2"
    assert vacancies_obj[2].alternate_url == "https://hh.ru/vacancy/108423996"
    assert vacancies_obj[2].responsibility == (
        "Участие в интересных проектах. Доработка и разработка программного "
        "комплекса. Дополнительно: Тестирование информационных систем. Настройка "
        "информационной системы (ИС) автоматизации бизнес-процессов. "
    )
    assert vacancies_obj[2].experience == "Нет опыта"


def test_filter_obj_vacancy_by_currency(vacancies_obj_list):
    filter_list = filter_obj_vacancy_by_currency(vacancies_obj_list)
    assert filter_list[0].name == "Программист"
    assert filter_list[0].currency == "RUR"
    assert filter_list[1].name == "Разработчик"
    assert filter_list[1].currency == "RUR"
    filter_list = filter_obj_vacancy_by_currency(vacancies_obj_list, "usd")
    assert filter_list[0].name == "Девелопер"
    assert filter_list[0].currency == "USD"
    assert filter_list[1].name == "Кодер"
    assert filter_list[1].currency == "USD"


def test_filter_obj_vacancy_by_experience_0(vacancies_obj_list):
    filter_list = filter_obj_vacancy_by_experience(vacancies_obj_list, "нет опыта")
    assert filter_list[0].name == "Программист"
    assert filter_list[0].currency == "RUR"


def test_filter_obj_vacancy_by_experience_1(vacancies_obj_list):
    filter_list = filter_obj_vacancy_by_experience(vacancies_obj_list, "от 1 года до 3 лет")
    assert filter_list[0].name == "Разработчик"
    assert filter_list[0].currency == "RUR"


def test_filter_obj_vacancy_by_experience_3(vacancies_obj_list):
    filter_list = filter_obj_vacancy_by_experience(vacancies_obj_list, "от 3 до 6 лет")
    assert filter_list[0].name == "Девелопер"
    assert filter_list[0].currency == "USD"


def test_filter_obj_vacancy_by_experience_6(vacancies_obj_list):
    filter_list = filter_obj_vacancy_by_experience(vacancies_obj_list, "более 6 лет")
    assert filter_list[0].name == "Кодер"
    assert filter_list[0].currency == "USD"
