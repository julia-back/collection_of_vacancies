from typing import Iterable, Any

import requests

from src.external_api import GetVacanciesAPI


class SearchVacanciesHH(GetVacanciesAPI):
    """Класс для Get-запросов на HeadHunter.ru"""

    def __init__(self, keywords: str) -> None:
        """
        Метод инициализации объекта для Get-запросов на HeadHunter.ru,
        принимает ключевые слова для посика вакансий
        """
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        keywords = keywords if keywords is not None else ""
        self.__params: dict[str, int | str] = {"page": 0, "per_page": 100, "text": keywords}
        self.__status_code = None
        self.__vacancies: list[Any] = []

    def _request(self) -> None:
        """Метод Get-запроса на HeadHunter.ru"""
        self.__status_code = None
        try:
            response = requests.get(url=self.__url, headers=self.__headers, params=self.__params)
        except TypeError as error:
            print(f"{error} in {__file__}")
        else:
            self.__status_code = response.status_code
            if self.__status_code == 200:
                new_vacancies = response.json().get("items")
                self.__vacancies.extend(new_vacancies)

    def get_vacancies(self) -> Iterable:
        """Метод получения вакансий с HeadHunter.ru"""
        while self.__params.get("page") < 20:
            self._request()
            self.__params["page"] += 1
        return self.__vacancies
