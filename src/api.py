from abc import ABC, abstractmethod

from requests import get


class AbstractAPI(ABC):

    @abstractmethod
    def get_aeroplanes(self, country):
        pass


class AeroplanesAPI(AbstractAPI):

    def __init__(self):
        self.__openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.__opensky_url = "https://opensky-network.org/api/states/all?"

    def get_aeroplanes(self, country: str):
        """
        Метод для получения данных о самолетах в определенной стране.
        """
        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        # Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        headers_nominatim = {
            "User-Agent": "test-app/1.0",
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            "country": country,
            "format": "json",
            "limit": 1,
        }

        response = get(url=self.__openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        # Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        geo_coordinates = data[0].get("boundingbox")

        # Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            "lamin": geo_coordinates[0],
            "lamax": geo_coordinates[1],
            "lomin": geo_coordinates[2],
            "lomax": geo_coordinates[3],
        }

        response = get(url=self.__opensky_url, params=params)

        # Пример ответа от opensky-network можно посмотреть в задании курсовой.
        return response.json()["states"]
