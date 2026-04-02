import pytest

from src.aeroplanes import Aeroplane

TEST_DATA = [
    ["A12", "SU1234", "Russia", "X", "Y", "Z", "1000", 8000, "W", 250],
    ["B34", "SD1000", "USA", "X", "Y", "Z", "2000", 12000, "W", 300],
    ["C56", "TR5678", "Russia", "X", "Y", "Z", "3000", 5000, "W", 200],
]


@pytest.fixture
def sample_aeroplanes():
    """Фикстура для создания списка самолётов"""
    Aeroplane.result.clear()
    return Aeroplane.cast_to_object_list(TEST_DATA)


def test_init():
    """Тест инициализации объекта"""
    plane = Aeroplane("TEST123", "Russia", 250, 8000)
    assert plane.callsign == "TEST123"
    assert plane.country == "Russia"
    assert plane.velocity == 250
    assert plane.baro_altitude == 8000


def test_str_representation():
    """Тест строкового представления объекта"""
    plane = Aeroplane("SU1234", "Russia", 250, 8000)
    expected = 'callsign: "SU1234", country: "Russia", velocity: 250, baro_altitude: 8000\n'
    assert str(plane) == expected


def test_cast_to_object_list(sample_aeroplanes):
    """Тест метода cast_to_object_list"""
    assert len(sample_aeroplanes) == 3

    # Первый самолёт
    first = sample_aeroplanes[0]
    assert first.callsign == "SU1234"
    assert first.country == "Russia"
    assert first.velocity == 250
    assert first.baro_altitude == 8000

    # Второй самолёт
    second = sample_aeroplanes[1]
    assert second.callsign == "SD1000"
    assert second.country == "USA"
    assert second.velocity == 300
    assert second.baro_altitude == 12000


def test_top_aeroplanes(sample_aeroplanes):
    """Тест метода top_aeroplanes"""
    top_2 = Aeroplane.top_aeroplanes(2, sample_aeroplanes)
    assert len(top_2) == 2
    assert top_2[0].callsign == "SU1234"
    assert top_2[1].callsign == "SD1000"

    # С числом больше длины списка
    top_5 = Aeroplane.top_aeroplanes(5, sample_aeroplanes)
    assert len(top_5) == 3


def test_getitem(sample_aeroplanes):
    """Тест доступа по индексу"""
    plane_instance = Aeroplane()

    first_plane_str = plane_instance[0]
    assert "SU1234" in first_plane_str
    assert "Russia" in first_plane_str

    last_plane_str = plane_instance[2]
    assert "TR5678" in last_plane_str
    assert "Russia" in last_plane_str


def test_filter_country(sample_aeroplanes):
    """Тест фильтрации по стране"""
    russian_planes = Aeroplane.filter_country("Russia", sample_aeroplanes)
    assert len(russian_planes) == 2
    assert all(plane.country == "Russia" for plane in russian_planes)
    assert russian_planes[0].callsign == "SU1234"
    assert russian_planes[1].callsign == "TR5678"

    usa_planes = Aeroplane.filter_country("USA", sample_aeroplanes)
    assert len(usa_planes) == 1
    assert usa_planes[0].callsign == "SD1000"


def test_filter_altitude_range(sample_aeroplanes):
    """Тест фильтрации по высоте"""
    high_planes = Aeroplane.filter_altitude_range(4000, sample_aeroplanes)
    assert len(high_planes) == 3  # SU1234 (8000) и TR5678 (5000)
    assert high_planes[0].callsign == "SU1234"
    assert high_planes[1].callsign == "SD1000"
    assert high_planes[2].callsign == "TR5678"

    very_high_planes = Aeroplane.filter_altitude_range(10000, sample_aeroplanes)
    assert len(very_high_planes) == 1  # SD1000 (12000)
    assert very_high_planes[0].callsign == "SD1000"


def test_empty_data():
    """Тест с пустыми данными"""
    Aeroplane.result.clear()
    empty_list = Aeroplane.cast_to_object_list([])
    assert len(empty_list) == 0

    # Топ с пустым списком
    top_result = Aeroplane.top_aeroplanes(2, [])
    assert len(top_result) == 0

    # Фильтрация по стране с пустым списком
    filtered = Aeroplane.filter_country("Russia", [])
    assert len(filtered) == 0
