import json
import os
from abc import ABC, abstractmethod
from typing import Any, Iterable

from config import DATA_PATH


class FileReader(ABC):
    """Абстрактный класс для чтения файла"""

    @abstractmethod
    def read_file(self) -> Any:
        """Абстрактный метод для чтения файла"""
        pass


class FileRewriter(ABC):
    """Абстрактный класс для перезаписи файла"""

    @abstractmethod
    def rewrite_file(self) -> None:
        """Абстрактный метод для перезаписи файла"""
        pass


class FileAppender(ABC):
    """Абстрактный класс для добавления данных в файл"""

    @abstractmethod
    def append_in_file(self, data: Any) -> None:
        """Абстрактный метод для добавления данных в файл"""
        pass

    @abstractmethod
    def clear_file(self) -> None:
        """Абстрактный метод для удаления всех данных из файла"""
        pass


class ReaderJSON(FileReader):
    """Класс для чтения JSON-файла"""

    def __init__(self, file_name: str = os.path.join(DATA_PATH, "vacancies_hh.json")) -> None:
        """Метод для инициализации объекта для чтения JSON-файла, принимает путь до файла опционально"""
        self.__file_name: str = file_name

    def read_file(self) -> Any:
        """Метод для чтения JSON-файла"""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            json_data = json.load(file)
        return json_data


class RewriterJSON(FileRewriter):
    """Класс для перезаписи JSON-файла"""

    def rewrite_file(self) -> None:
        """Метод для перезаписи JSON-файла"""
        pass


class AppenderInJSON(FileAppender):
    """Класс для добавления данных в JSON-файл"""

    def __init__(self, file_name: str = os.path.join(DATA_PATH, "vacancies_hh.json")) -> None:
        """Метод инициализации объекта для добавления данных в JSON-файл, принимает путь до файла опционльно"""
        self.__file_name = file_name

    def append_in_file(self, data: Iterable[Any]) -> None:
        """Метод для добавления данных в JSON-файл (список)"""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            json_data.extend(data)
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

    def clear_file(self) -> None:
        """Метод для удаления всех данных из JSON-файла, оставляет пустой список"""
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump([], file)
