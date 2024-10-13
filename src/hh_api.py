import json

import requests
import os
from config import DATA_PATH
from src.external_api import GetVacanciesAPI


class SearchVacanciesHH(GetVacanciesAPI):

    def __init__(self, keywords: str):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        keywords = keywords if keywords is not None else ""
        self.__params = {"page": 0, "per_page": 100, "text": keywords}
        self.__status_code = None
        self.__vacancies = []

    def _request(self):
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

    def get_vacancies(self):
        while self.__params.get("page") < 20:
            self._request()
            self.__params["page"] += 1
        return self.__vacancies
