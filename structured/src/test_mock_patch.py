def get_sensor_temp(sensor):
    return sensor.read_value()

from unittest.mock import Mock

def test_get_sensor_value():
    fake_sensor = Mock()
    fake_sensor.read_value.return_value = 98 #F
    assert get_sensor_temp(fake_sensor) == 98 #F


import os
def check_data_file():
    return os.path.exists("data.bin")

from unittest.mock import patch

def test_check_data_file():
    with patch("os.path.exists", return_value=True):
        assert check_data_file() is True


import pytest

class DummySensor:
    def __init__(self):
        self.value = 99
    def read_value(self):
        return self.value

@pytest.fixture
def dummy_sensor():
    return DummySensor()

def test_dummy_sensor(dummy_sensor):
    assert dummy_sensor.read_value() == 99
