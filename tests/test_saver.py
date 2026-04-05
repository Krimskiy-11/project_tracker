import os
from src.saver import JSONSaver
from src.aeroplanes import Aeroplane


class TestJSONSaver:
    def setup_method(self):
        """Подготовка перед тестом."""
        self.saver = JSONSaver("test.json")
        # Удаляем файл, если он существует
        if os.path.exists(self.saver._JSONSaver__file_path):
            os.remove(self.saver._JSONSaver__file_path)

    def teardown_method(self):
        """Очистка после теста."""
        if os.path.exists(self.saver._JSONSaver__file_path):
            os.remove(self.saver._JSONSaver__file_path)

    def test_save_and_load(self):
        """Тест сохранения и загрузки данных."""
        plane = Aeroplane("TEST123", "TestCountry", 100.0, 1500.0)
        self.saver.add_aeroplane([plane])

        data = self.saver.get_aeroplanes_from_file()
        assert data[0]["callsign"] == "TEST123"

    def test_no_duplicates(self):
        """Тест предотвращения дубликатов."""
        plane = Aeroplane("DUPE123", "Test", 50.0, 1000.0)

        self.saver.add_aeroplane([plane])
        self.saver.add_aeroplane([plane])

        data = self.saver.get_aeroplanes_from_file()
        assert len(data) == 1

    def test_add_new_data(self):
        """Тест добавления новых данных."""
        plane1 = Aeroplane("FLT100", "Country1", 200.0, 3000.0)
        plane2 = Aeroplane("FLT200", "Country2", 250.0, 4000.0)

        self.saver.add_aeroplane([plane1])
        self.saver.add_aeroplane([plane2])

        data = self.saver.get_aeroplanes_from_file()
        assert len(data) == 2
        assert data[1]["callsign"] == "FLT200"

    def test_remove_plane(self):
        """Тест удаления самолёта."""
        plane = Aeroplane("REM123", "Remove", 10.0, 500.0)
        self.saver.add_aeroplane([plane])

        result = self.saver.remove_aeroplane("REM123")
        assert result is True

        data = self.saver.get_aeroplanes_from_file()
        assert len(data) == 0

    def test_empty_file(self):
        """Тест чтения пустого файла."""
        data = self.saver.get_aeroplanes_from_file()
        assert data == []
