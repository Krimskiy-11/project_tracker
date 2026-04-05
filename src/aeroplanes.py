class Aeroplane:
    """Класс для работы с информацией о самолетах."""

    __slots__ = ("callsign", "country", "velocity", "baro_altitude")

    result = []

    def __init__(self, callsign=None, country=None, velocity=None, baro_altitude=None):
        self.callsign = self._validate_callsign(callsign)
        self.country = self._validate_country(country)
        self.velocity = self._validate_velocity(velocity)
        self.baro_altitude = self._validate_baro_altitude(baro_altitude)

    def _validate_callsign(self, callsign):
        """Приватный метод валидации позывного."""
        if callsign is None:
            return "Unknown"
        if not isinstance(callsign, str):
            raise ValueError("Callsign must be a string")
        return callsign.strip()

    def _validate_country(self, country):
        """Приватный метод валидации страны."""
        if country is None:
            return "Unknown"
        if not isinstance(country, str):
            raise ValueError("Country must be a string")
        return country.strip()

    def _validate_velocity(self, velocity):
        """Приватный метод валидации скорости."""
        if velocity is None:
            return 0.0
        if isinstance(velocity, (int, float)) and velocity >= 0:
            return float(velocity)
        raise ValueError("Velocity must be a non-negative number")

    def _validate_baro_altitude(self, baro_altitude):
        """Приватный метод валидации высоты."""
        if baro_altitude is None:
            return None
        if isinstance(baro_altitude, (int, float)):
            return float(baro_altitude)
        raise ValueError("Baro altitude must be a number")

    def __str__(self):
        return (
            f'callsign: "{self.callsign}", '
            f'country: "{self.country}", '
            f"velocity: {self.velocity}, "
            f"baro_altitude: {self.baro_altitude}\n"
        )

    @classmethod
    def cast_to_object_list(cls, country_aeroplanes):
        """
        Метод для определения атрибутов:
            позывной,
            страна регистрации,
            скорость полета (м/с),
            высота полета (м).
        """
        for item in country_aeroplanes:
            callsign = item[1]
            country = item[2]
            velocity = item[9]
            baro_altitude = item[7]
            one_aeroplane = cls(callsign, country, velocity, baro_altitude)
            cls.result.append(one_aeroplane)

        return cls.result

    @classmethod
    def top_aeroplanes(cls, top: int, aeroplane):
        """
        Метод для вывода топ N самолетов.
        """
        return aeroplane[:top]

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self) -> str:
        if self.value + 1 < len(Aeroplane.result):
            self.value += 1
            return str(Aeroplane.result[self.value])
        else:
            raise StopIteration

    def __getitem__(self, item):
        return str(Aeroplane.result[item])

    @classmethod
    def filter_country(cls, country: str, aeroplane):
        """
        Метод для фильтрации самолетов по стране регистрации.
        """
        res = []
        for item in aeroplane:
            if item.country == country:
                res.append(item)
        return res

    def __ge__(self, other):
        """
        Магический метод для сравнения самолётов по высоте (больше или равно).
        """
        if isinstance(other, Aeroplane):
            return self.baro_altitude >= other.baro_altitude
        elif isinstance(other, (int, float)):
            return self.baro_altitude >= other
        return NotImplemented

    @classmethod
    def filter_altitude_range(cls, altitude: int, aeroplanes):
        """
        Метод для фильтрации самолётов по высоте полёта (больше или равно заданной).
        Использует магический метод __ge__.
        """
        return [item for item in aeroplanes if item.baro_altitude is not None and item >= altitude]


# {
#     "time": 1766142246,                 // UNIX-время сервера OpenSky (секунды)
#     "states": [
#         [
#             "4b1812",                   // ICAO24 — уникальный идентификатор борта
#             "SWR438A ",                 // Callsign — позывной рейса
#             "Switzerland",             // Страна регистрации ВС
#             1766166618,                 // time_position — время последнего обновления позиции
#             1766166618,                 // last_contact — время последнего контакта
#             -0.0168,                    // longitude — долгота (°)
#             51.0888,                    // latitude — широта (°)
#             4267.2,                    // baro_altitude — барометрическая высота (м)
#             false,                     // on_ground — находится ли самолёт на земле
#             189.7,                    // velocity — горизонтальная скорость (м/с)
#             129.39,                     // true_track — курс (градусы)
#             14.63,                     // vertical_rate — вертикальная скорость (м/с)
#             null,                      // sensors — ID сенсоров (null = неизвестно)
#             4282.44,                  // geo_altitude — геометрическая высота (м)
#             "2061",                   // squawk — код ответчика (транспондера)
#             false,                    // spi — специальный сигнал (emergency/priority)
#             0                          // position_source — источник позиции
#         ],
#         ...
#     ]
# }
