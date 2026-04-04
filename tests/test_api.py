from unittest.mock import Mock, patch

from src.api import AeroplanesAPI


class TestAeroplanesAPI:
    @patch('requests.get')
    def test_successful_request(self, mock_get):
        """Тест успешного получения данных."""
        # Мок для OpenStreetMap
        mock_osm = Mock()
        mock_osm.status_code = 200
        mock_osm.json.return_value = [{"boundingbox": ["1", "2", "3", "4"]}]

        # Мок для OpenSky
        mock_opensky = Mock()
        mock_opensky.status_code = 200
        mock_opensky.json.return_value = {"states": [["test_data"]]}

        mock_get.side_effect = [mock_osm, mock_opensky]

        api = AeroplanesAPI()
        result = api.get_aeroplanes("Germany")

        assert result == [["test_data"]]
