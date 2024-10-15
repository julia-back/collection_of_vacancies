from src.vacancies import Vacancy


def test_vacancy_init(vacancies_obj_list):
    assert vacancies_obj_list[0].id_ == 108001774
    assert vacancies_obj_list[0].name == "Программист"
    assert vacancies_obj_list[0].area == "Москва"
    assert vacancies_obj_list[0].salary_from == 10000
    assert vacancies_obj_list[0].salary_to == 20000
    assert vacancies_obj_list[0].currency == "RUR"
    assert vacancies_obj_list[0].address == "Пшеничная, 10"
    assert vacancies_obj_list[0].alternate_url == "url"
    assert vacancies_obj_list[0].responsibility == "Круто программировать"
    assert vacancies_obj_list[0].experience == "Нет опыта"

    assert len(Vacancy.vacancies) == 4

    assert vacancies_obj_list[0] < vacancies_obj_list[1]
    assert vacancies_obj_list[1] > vacancies_obj_list[0]
    assert vacancies_obj_list[0] <= vacancies_obj_list[1]
    assert vacancies_obj_list[1] > vacancies_obj_list[0]
    assert vacancies_obj_list[0] != vacancies_obj_list[1]
    assert vacancies_obj_list[0] != 5000
    assert vacancies_obj_list[0] == 10000
    assert vacancies_obj_list[0] <= 5000000
    assert vacancies_obj_list[0] >= 5000
    assert vacancies_obj_list[0] < 5000000
    assert vacancies_obj_list[0] > 5000

    Vacancy.delite_vacancy(vacancies_obj_list[0])
    assert len(Vacancy.vacancies) == 3
