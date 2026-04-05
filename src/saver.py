import os
import json
from abc import ABC, abstractmethod


class AbstractJSON(ABC):
    @abstractmethod
    def add_aeroplane(self, vacancy):
        pass

    @abstractmethod
    def get_aeroplanes_from_file(self):
        pass

    @abstractmethod
    def remove_aeroplane(self, callsign):
        pass


class JSONSaver(AbstractJSON):
    def __init__(self, file_name="aeroplanes.json"):
        self.__file_name = file_name
        high_path = os.path.dirname(os.path.dirname(__file__))
        self.__file_path = os.path.join(high_path, "data", self.__file_name)
        os.makedirs(os.path.dirname(self.__file_path), exist_ok=True)

    def add_aeroplane(self, vacancy):
        """
        Добавляет данные в файл без перезаписи, избегая дубликатов.
        """
        existing_data = self.get_aeroplanes_from_file()
        new_data = []

        for plane in vacancy:
            # Проверяем, есть ли уже такой самолёт (по позывному)
            if not any(p.get("callsign") == plane.callsign for p in existing_data):
                new_data.append(
                    {
                        "callsign": plane.callsign,
                        "country": plane.country,
                        "velocity": plane.velocity,
                        "baro_altitude": plane.baro_altitude,
                    }
                )

        # Объединяем существующие и новые данные
        combined_data = existing_data + new_data

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(combined_data, f, ensure_ascii=False, indent=4)

    def get_aeroplanes_from_file(self):
        """Получает данные из файла."""
        if not os.path.exists(self.__file_path):
            return []
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError, IOError:
            return []

    def remove_aeroplane(self, callsign: str):
        """Удаляет самолёт из файла по позывному."""
        data = self.get_aeroplanes_from_file()
        filtered_data = [plane for plane in data if plane.get("callsign") != callsign]

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)

        return len(data) > len(filtered_data)  # True, если что-то удалили

        # f.write(str(vacancy))
