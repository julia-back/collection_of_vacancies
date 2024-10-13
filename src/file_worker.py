from abc import ABC, abstractmethod
import os
from config import DATA_PATH
import json


class FileReader(ABC):

    @abstractmethod
    def read_file(self):
        pass


class FileRewriter(ABC):

    @abstractmethod
    def rewrite_file(self):
        pass


class FileAppender(ABC):

    @abstractmethod
    def append_in_file(self, data):
        pass

    @abstractmethod
    def clear_file(self):
        pass


class ReaderJSON(FileReader):

    def __init__(self, file_name=os.path.join(DATA_PATH, "vacancies_hh.json")):
        self.__file_name = file_name

    def read_file(self):
        with open(self.__file_name, "r", encoding="utf-8") as file:
            json_data = json.load(file)
        return json_data


class RewriterJSON(FileRewriter):

    def rewrite_file(self):
        pass


class AppenderInJSON(FileAppender):

    def __init__(self, file_name=os.path.join(DATA_PATH, "vacancies_hh.json")):
        self.__file_name = file_name

    def append_in_file(self, data: list):
        with open(self.__file_name, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            json_data.extend(data)
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

    def clear_file(self):
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump([], file)
