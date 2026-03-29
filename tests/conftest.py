import pytest

from src.api import AeroplanesAPI


@pytest.fixture
def api():
    return AeroplanesAPI()
