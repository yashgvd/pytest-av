from vehicle_utils import compute_speed
import pytest
import time


def test_compute_speed_basic():
    # 1024 ticks = 1 revolution, circumference = 2m, interval = 1s
    assert compute_speed(1024, 1, 2) == 2.0

def test_compute_speed_zero_ticks():
    assert compute_speed(0, 1, 2) == 0

def test_compute_speed_negative_interval():
    with pytest.raises(ValueError):
        compute_speed(1024, 0, 2)

def test_compute_speed_negative_circumference():
    with pytest.raises(ValueError):
        compute_speed(1024, 1, -1)
        
def test_compute_speed_large_ticks():
    assert compute_speed(1024000, 1000, 2) == 2.0  # 1000 revolutions in 1000s = 2m/s

def test_compute_speed_float_ticks():
    with pytest.raises(ValueError):
        compute_speed(512.5, 1, 2) 

def test_compute_speed_str_ticks():
    with pytest.raises(ValueError):
        compute_speed("1024", 1, 2) 

def test_compute_speed_performance():
    start = time.time()
    for _ in range(10000):
        compute_speed(1024, 1, 2)
    duration = time.time() - start
    # Assert total time is <0.1s for 10,000 runs (i.e., <0.01ms per call)
    assert duration < 0.1
