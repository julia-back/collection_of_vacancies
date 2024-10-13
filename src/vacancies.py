class Vacancy:

    vacancies = []

    __slots__ = ("id_", "name", "area", "salary_from", "salary_to", "currency",
                 "address", "alternate_url", "responsibility", "experience")

    def __init__(self, id_: str, name: str, area: str, salary_from: int | float, salary_to: int | float, currency: str,
                 address: str, alternate_url: str, responsibility: str, experience: str):
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

    def __eq__(self, other):
        """Метод для определния равенства по атрибуту salary_from"""
        other = self.__get_num_for_compare(other)
        return self.salary_from == other

    def __lt__(self, other):
        """Метод для сравнения '<' по атрибуту salary_from"""
        other = self.__get_num_for_compare(other)
        return self.salary_from < other

    def __le__(self, other):
        """Метод для сравнения '<=' по атрибуту salary_from"""
        other = self.__get_num_for_compare(other)
        return self.salary_from <= other

    def __is_exclude(self):
        for vacancy in Vacancy.vacancies:
            if vacancy.id_ == self.id_:
                return False
        return True

    @classmethod
    def delite_vacancy(cls, obj_for_del):
        cls.vacancies.remove(obj_for_del)

    @staticmethod
    def __get_num_for_compare(other):
        if isinstance(other, (int, float)):
            other = other
        elif isinstance(other, Vacancy):
            other = other.salary_from
        else:
            raise TypeError("Сравнить можно с числом или другим объектом класса Vacancy")
        return other
