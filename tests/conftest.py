import pytest

from src.vacancies import Vacancy


@pytest.fixture
def vacancies_hh_json():
    return {
        "items": [
            {
                "id": "108001774",
                "premium": False,
                "name": "Junior Python разработчик",
                "department": None,
                "has_test": False,
                "response_letter_required": True,
                "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
                "salary": {"from": 125000, "to": None, "currency": "RUR", "gross": False},
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-10-01T14:57:35+0300",
                "created_at": "2024-10-01T14:57:35+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108001774",
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/108001774?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/108001774",
                "relations": [],
                "employer": {
                    "id": "11075572",
                    "name": "Monogramm",
                    "url": "https://api.hh.ru/employers/11075572",
                    "alternate_url": "https://hh.ru/employer/11075572",
                    "logo_urls": None,
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11075572",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Базовые знания <highlighttext>Python</highlighttext>."
                    " Понимание ООП. Опыт работы с фреймворками (например, Django, Flask)."
                    " Знание SQL. Базовые знания HTML, CSS, JavaScript. ",
                    "responsibility": "Разработка и поддержка backend части приложения на"
                    " <highlighttext>Python</highlighttext>. Работа с базами"
                    " данных (например, PostgreSQL, MongoDB). Написание чистого,"
                    " эффективного и хорошо...",
                },
                "contacts": None,
                "schedule": {"id": "flexible", "name": "Гибкий график"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "108291622",
                "premium": False,
                "name": "Программист - разработчик Junior - .NET C# ASP Java",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "1003", "name": "Гомель", "url": "https://api.hh.ru/areas/1003"},
                "salary": {"from": 150, "to": 600, "currency": "USD", "gross": False},
                "type": {"id": "open", "name": "Открытая"},
                "address": None,
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-10-07T16:56:02+0300",
                "created_at": "2024-10-07T16:56:02+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108291622",
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/108291622?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/108291622",
                "relations": [],
                "employer": {
                    "id": "804583",
                    "name": "Услуги 22 век, ЧП",
                    "url": "https://api.hh.ru/employers/804583",
                    "alternate_url": "https://hh.ru/employer/804583",
                    "logo_urls": None,
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=804583",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Приветствуется одновременное умение применять другие языки"
                    " технологии (по убыванию приоритетности: PHP, C++, Python)."
                    " Уверенное владение PHP (можно без объектного подхода). ",
                    "responsibility": "Выполнение заданий разнообразного характера (структуры данных"
                    " и алгоритмы, базовый CRUD, клиент-серверные приложения, работа"
                    " с СУБД, веб-приложения). ",
                },
                "contacts": None,
                "schedule": {"id": "remote", "name": "Удаленная работа"},
                "working_days": [{"id": "only_saturday_and_sunday", "name": "По\xa0субботам и\xa0воскресеньям"}],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "part", "name": "Частичная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
            {
                "id": "108423996",
                "premium": False,
                "name": "Программист (Junior - младший разработчик)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "2", "name": "Санкт-Петербург", "url": "https://api.hh.ru/areas/2"},
                "salary": {"from": 30000, "to": 70000, "currency": "RUR", "gross": True},
                "type": {"id": "open", "name": "Открытая"},
                "address": {
                    "city": "Санкт-Петербург",
                    "street": "Мебельная улица",
                    "building": "12к2",
                    "lat": 59.990602,
                    "lng": 30.241793,
                    "description": None,
                    "raw": "Санкт-Петербург, Мебельная улица, 12к2",
                    "metro": {
                        "station_name": "Старая Деревня",
                        "line_name": "Фрунзенско-Приморская",
                        "station_id": "18.246",
                        "line_id": "18",
                        "lat": 59.989433,
                        "lng": 30.255163,
                    },
                    "metro_stations": [
                        {
                            "station_name": "Старая Деревня",
                            "line_name": "Фрунзенско-Приморская",
                            "station_id": "18.246",
                            "line_id": "18",
                            "lat": 59.989433,
                            "lng": 30.255163,
                        }
                    ],
                    "id": "120450",
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2024-10-09T16:16:03+0300",
                "created_at": "2024-10-09T16:16:03+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108423996",
                "show_logo_in_search": None,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/108423996?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/108423996",
                "relations": [],
                "employer": {
                    "id": "803096",
                    "name": "ПТМК",
                    "url": "https://api.hh.ru/employers/803096",
                    "alternate_url": "https://hh.ru/employer/803096",
                    "logo_urls": {
                        "240": "https://img.hhcdn.ru/employer-logo/3093877.png",
                        "90": "https://img.hhcdn.ru/employer-logo/3093876.png",
                        "original": "https://img.hhcdn.ru/employer-logo-original/663186.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=803096",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Знание одного из объектно-ориентированного языка программирования,"
                    " к примеру: C++\\C#, Delphi, Python, Pascal, 1С. Знание работы с"
                    " СУБД...",
                    "responsibility": "Участие в интересных проектах. Доработка и разработка"
                    " программного комплекса. Дополнительно: Тестирование"
                    " информационных систем. Настройка информационной системы"
                    " (ИС) автоматизации бизнес-процессов. ",
                },
                "contacts": None,
                "schedule": {"id": "fullDay", "name": "Полный день"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": True,
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "noExperience", "name": "Нет опыта"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
        ],
        "found": 294,
        "pages": 3,
        "page": 0,
        "per_page": 100,
        "clusters": None,
        "arguments": None,
        "fixes": None,
        "suggests": None,
        "alternate_url": "https://hh.ru/search/vacancy?enable_snippets=true&items_on_page=100&"
        "text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D"
        "0%B8%D0%BA+junior",
    }


@pytest.fixture
def vacancies_hh():
    return [
        {
            "id": "108001774",
            "premium": False,
            "name": "Junior Python разработчик",
            "department": None,
            "has_test": False,
            "response_letter_required": True,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 125000, "to": None, "currency": "RUR", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-10-01T14:57:35+0300",
            "created_at": "2024-10-01T14:57:35+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108001774",
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/108001774?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/108001774",
            "relations": [],
            "employer": {
                "id": "11075572",
                "name": "Monogramm",
                "url": "https://api.hh.ru/employers/11075572",
                "alternate_url": "https://hh.ru/employer/11075572",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11075572",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Базовые знания <highlighttext>Python</highlighttext>."
                " Понимание ООП. Опыт работы с фреймворками (например, Django, Flask)."
                " Знание SQL. Базовые знания HTML, CSS, JavaScript. ",
                "responsibility": "Разработка и поддержка backend части приложения на"
                " <highlighttext>Python</highlighttext>. Работа с базами"
                " данных (например, PostgreSQL, MongoDB). Написание чистого,"
                " эффективного и хорошо...",
            },
            "contacts": None,
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
        {
            "id": "108291622",
            "premium": False,
            "name": "Программист - разработчик Junior - .NET C# ASP Java",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1003", "name": "Гомель", "url": "https://api.hh.ru/areas/1003"},
            "salary": {"from": 150, "to": 600, "currency": "USD", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-10-07T16:56:02+0300",
            "created_at": "2024-10-07T16:56:02+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108291622",
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/108291622?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/108291622",
            "relations": [],
            "employer": {
                "id": "804583",
                "name": "Услуги 22 век, ЧП",
                "url": "https://api.hh.ru/employers/804583",
                "alternate_url": "https://hh.ru/employer/804583",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=804583",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Приветствуется одновременное умение применять другие языки"
                " технологии (по убыванию приоритетности: PHP, C++, Python)."
                " Уверенное владение PHP (можно без объектного подхода). ",
                "responsibility": "Выполнение заданий разнообразного характера (структуры данных"
                " и алгоритмы, базовый CRUD, клиент-серверные приложения, работа"
                " с СУБД, веб-приложения). ",
            },
            "contacts": None,
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [{"id": "only_saturday_and_sunday", "name": "По\xa0субботам и\xa0воскресеньям"}],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "part", "name": "Частичная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
        {
            "id": "108423996",
            "premium": False,
            "name": "Программист (Junior - младший разработчик)",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "2", "name": "Санкт-Петербург", "url": "https://api.hh.ru/areas/2"},
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Санкт-Петербург",
                "street": "Мебельная улица",
                "building": "12к2",
                "lat": 59.990602,
                "lng": 30.241793,
                "description": None,
                "raw": "Санкт-Петербург, Мебельная улица, 12к2",
                "metro": {
                    "station_name": "Старая Деревня",
                    "line_name": "Фрунзенско-Приморская",
                    "station_id": "18.246",
                    "line_id": "18",
                    "lat": 59.989433,
                    "lng": 30.255163,
                },
                "metro_stations": [
                    {
                        "station_name": "Старая Деревня",
                        "line_name": "Фрунзенско-Приморская",
                        "station_id": "18.246",
                        "line_id": "18",
                        "lat": 59.989433,
                        "lng": 30.255163,
                    }
                ],
                "id": "120450",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-10-09T16:16:03+0300",
            "created_at": "2024-10-09T16:16:03+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108423996",
            "show_logo_in_search": None,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/108423996?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/108423996",
            "relations": [],
            "employer": {
                "id": "803096",
                "name": "ПТМК",
                "url": "https://api.hh.ru/employers/803096",
                "alternate_url": "https://hh.ru/employer/803096",
                "logo_urls": {
                    "240": "https://img.hhcdn.ru/employer-logo/3093877.png",
                    "90": "https://img.hhcdn.ru/employer-logo/3093876.png",
                    "original": "https://img.hhcdn.ru/employer-logo-original/663186.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=803096",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Знание одного из объектно-ориентированного языка программирования,"
                " к примеру: C++\\C#, Delphi, Python, Pascal, 1С. Знание работы с"
                " СУБД...",
                "responsibility": "Участие в интересных проектах. Доработка и разработка"
                " программного комплекса. Дополнительно: Тестирование"
                " информационных систем. Настройка информационной системы"
                " (ИС) автоматизации бизнес-процессов. ",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": True,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
    ]


@pytest.fixture
def vacancies_dicts_by_keys():
    return [
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


@pytest.fixture
def vacancies_obj_list():
    Vacancy.vacancies = []
    return [
        Vacancy(108001774, "Программист", "Москва", 10000, 20000, "RUR",
                "Пшеничная, 10", "url", "Круто программировать", "Нет опыта",),
        Vacancy(108001775, "Разработчик", "Казань", 20000, 30000, "RUR",
                "", "url", "Круто разрабатывать", "От 1 года до 3 лет"),
        Vacancy(108001776, "Девелопер", "Питер", 30000, 40000, "USD",
                "", "url", "Круто писать код", "От 3 до 6 лет"),
        Vacancy(108001777, "Кодер", "Кострома", 40000, 50000, "USD",
                "", "url", "Круто кодить", "Более 6 лет"),
    ]
