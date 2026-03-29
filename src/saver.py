import os


class JSONSaver:

    @classmethod
    def add_aeroplane(cls, vacancy):
        """
        Метод для сохранения данных в JSON-файл.
        """
        high_path = os.path.dirname(os.path.dirname(__file__))  # C:\projects\Project_tracker
        path_data = os.path.join(high_path, "data")  # C:\projects\Project_tracker\data
        path_file = os.path.join(path_data, "aeroplanes.json")

        with open(path_file, "w") as f:
            for plane in vacancy:
                f.write(str(plane))
