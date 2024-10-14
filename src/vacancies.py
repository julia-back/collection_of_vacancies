class Vacancy:
    """Класс для работы с вакансиями"""

    vacancies: list = []

    __slots__ = ("id_", "name", "area", "salary_from", "salary_to", "currency",
                 "address", "alternate_url", "responsibility", "experience")

    def __init__(self, id_: str | int, name: str, area: str, salary_from: int | float,
                 salary_to: int | float, currency: str,
                 address: str, alternate_url: str, responsibility: str, experience: str) -> None:
        """Метод инизиализации объектов класса"""
        self.id_ = id_
        self.name = name
        self.area = area
        self.salary_from = salary_from if salary_from is not None else 0
        self.salary_to = salary_to if salary_to is not None else 0
        self.currency = currency if currency is not None else "RUR"
        self.address = address if address is not None else "NoAddress"
        self.alternate_url = alternate_url
        self.responsibility = responsibility
        self.experience = experience
        if self.__is_exclude():
            Vacancy.vacancies.append(self)

    def __eq__(self, other: int | float | object) -> bool:
        """Метод для определния равенства по атрибуту salary_from"""
        other_num = self.__get_num_for_compare(other)
        self_num = self.__get_num_for_compare(self)
        return self_num == other_num

    def __lt__(self, other: int | float | object) -> bool:
        """Метод для сравнения '<' по атрибуту salary_from"""
        other_num = self.__get_num_for_compare(other)
        self_num = self.__get_num_for_compare(self)
        return self_num < other_num

    def __le__(self, other: int | float | object) -> bool:
        """Метод для сравнения '<=' по атрибуту salary_from"""
        other_num = self.__get_num_for_compare(other)
        self_num = self.__get_num_for_compare(self)
        return self_num <= other_num

    def __is_exclude(self) -> bool:
        """Поиск дубликатов вакансии в общем списке вакансий"""
        for vacancy in Vacancy.vacancies:
            if vacancy.id_ == self.id_:
                return False
        return True

    @classmethod
    def delite_vacancy(cls, obj_for_del: object) -> None:
        """Метод удаления вакансии из общего списка вакансий"""
        cls.vacancies.remove(obj_for_del)

    @staticmethod
    def __get_num_for_compare(other: int | float | object) -> int | float:
        """Приватный метод для получения числа для сравнения, принимает объект класса или число int/float"""
        if isinstance(other, (int, float)):
            other = other
        elif isinstance(other, Vacancy):
            other = other.salary_from
        else:
            raise TypeError("Сравнить можно с числом или другим объектом класса Vacancy")
        return other
