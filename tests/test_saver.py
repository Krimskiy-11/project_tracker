import os

from src.saver import JSONSaver


def test_data_written():
    planes = [{"callsign": "VOE1AT", "country": "Spain", "velocity": 213, "baro_altitude": 8732}]
    JSONSaver.add_aeroplane(planes)

    high_path = os.path.dirname(os.path.dirname(__file__))  # C:\projects\Project_tracker
    path_data = os.path.join(high_path, "data")  # C:\projects\Project_tracker\data
    path_file = os.path.join(path_data, "aeroplanes.json")

    with open(path_file, "r") as f:
        content = f.read()

    assert str("{'callsign': 'VOE1AT', 'country': 'Spain', 'velocity': 213, 'baro_altitude': " "8732}") in content
