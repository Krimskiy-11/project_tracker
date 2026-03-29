from unittest.mock import Mock, patch


@patch("src.api.get")
def test_get_aeroplanes(mock_get, api):
    """Тест получения данных о самолётах."""

    mock_nominatim = Mock()
    mock_nominatim.json.return_value = [{"boundingbox": ["10", "20", "30", "40"]}]

    mock_opensky = Mock()
    mock_opensky.json.return_value = {"states": [["plane1"], ["plane2"]]}

    mock_get.side_effect = [mock_nominatim, mock_opensky]

    result = api.get_aeroplanes("Netherlands")

    assert result == [["plane1"], ["plane2"]]
    assert mock_get.call_count == 2
