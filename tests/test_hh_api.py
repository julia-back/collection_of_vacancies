from src.hh_api import SearchVacanciesHH
from unittest.mock import patch


@patch("requests.get")
def test_search_vacancies(mock_get, vacancies_hh_for_get, vacancies_hh_json_after_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = vacancies_hh_for_get
    hh_api = SearchVacanciesHH("")
    assert hh_api.get_vacancies() == vacancies_hh_json_after_get
