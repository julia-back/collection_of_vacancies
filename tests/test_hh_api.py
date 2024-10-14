# from src.hh_api import SearchVacanciesHH
# from unittest.mock import patch
#
#
# @patch("requests.get")
# def test_search_vacancies(mock_get, vacancies_hh_json):
#     mock_get.return_value.status_code.return_value = 200
#     mock_get.return_value.json.return_value = vacancies_hh_json
#     hh_api = SearchVacanciesHH("")
#     assert hh_api.get_vacancies() == ""
