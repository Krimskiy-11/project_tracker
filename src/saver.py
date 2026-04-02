import os
import json
from abc import abstractmethod, ABC


class AbstractJSON(ABC):
    @abstractmethod
    def add_aeroplane(self, vacancy):
        pass

class JSONSaver(AbstractJSON):
    @classmethod
    def add_aeroplane(cls, vacancy, file_path="aeroplanes.json"):
        high_path = os.path.dirname(os.path.dirname(__file__))
        path_data = os.path.join(high_path, "data")
        os.makedirs(path_data, exist_ok=True)
        path_file = os.path.join(path_data, file_path)

        with open(path_file, "w", encoding="utf-8") as f:
            # json.dump(vacancy, f, ensure_ascii=False, indent=4)
            for item in vacancy:
                f.write(str(item))
            # f.write(str(vacancy))
