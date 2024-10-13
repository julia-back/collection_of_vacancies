from abc import ABC, abstractmethod


class RequestAPI(ABC):

    @abstractmethod
    def _request(self):
        pass


class GetRequestAPI(RequestAPI, ABC):

    @abstractmethod
    def _request(self):
        pass


class PostRequestAPI(RequestAPI, ABC):

    @abstractmethod
    def _request(self):
        pass


class GetVacanciesAPI(GetRequestAPI, ABC):

    @abstractmethod
    def _request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
