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
        self.__is_connected = False


    def _connect(self, url: str, params: dict = None, headers: dict = None):
        """
        Приватный метод подключения к API.
        Отправляет запрос на базовый URL, проверяет статус-код ответа.
        """
        try:
            response = get(url=url, params=params, headers=headers)
            if response.status_code != 200:
                raise Exception(f"API error: {response.status_code}")
            self.__is_connected = True
            return response
        except Exception as e:
            self.__is_connected = False
            raise e

    def get_aeroplanes(self, country: str):
        """
        Метод для получения данных о самолетах в определенной стране.
        Вызывает метод подключения перед отправкой запроса.
        """
        # Получаем географические координаты через OpenStreetMap
        headers_nominatim = {"User-Agent": "test-app/1.0"}
        params_nominatim = {
            "country": country,
            "format": "json",
            "limit": 1,
        }

        response = self._connect(
            url=self.__openstreetmap_url,
            params=params_nominatim,
            headers=headers_nominatim
        )
        data = response.json()

        if not data:
            raise ValueError(f"No data found for country: {country}")

        geo_coordinates = data[0].get("boundingbox")
        if not geo_coordinates:
            raise ValueError("Bounding box not found in OpenStreetMap response")

        # Параметры для фильтрации самолётов по координатам
        params = {
            "lamin": geo_coordinates[0],
            "lamax": geo_coordinates[1],
            "lomin": geo_coordinates[2],
            "lomax": geo_coordinates[3],
        }

        # Подключение к OpenSky API
        response = self._connect(url=self.__opensky_url, params=params)
        return response.json().get("states", [])
