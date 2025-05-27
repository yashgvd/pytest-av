from src.state_utils import parse_vehicle_state
from src.time_utils import is_monotonic
import pytest
import random
import os 
import time
import sys

@pytest.mark.slow
def test_slow():
    time.sleep(3)
    a = 1+1
    del a
    assert True

@pytest.mark.integration
def test_int():
    time.sleep(3)
    assert 1+1 == 2

@pytest.mark.skipif(sys.platform == 'linux', reason="Only compiled for windows")
def test_skip():
    a = 1+1
    del a
    return True

@pytest.mark.xfail(reason="Not integrated yet")
def test_fail():
    assert 1 == 0

@pytest.mark.skip(reason="Test skip")
def test_fail():
    assert 1 == 0


@pytest.fixture
def log_file_gen():
    ts = 0
    path = 'temp_log.txt'
    print("Creating temp log")
    with open(path,'w') as f:
        for _ in range(100):
            ts += random.uniform(0.5,1)
            f.write(f"{ts}\n")
    yield path
    print("Deleting temp log")
    os.remove('temp_log.txt')

def test_fixture(log_file_gen):
    all_ts = []
    with open(log_file_gen,'r') as f:
        for i in f:
            all_ts.append(float(i.strip()))
    assert is_monotonic(all_ts) == True
            
    

@pytest.mark.parametrize("state_dict, vehicle_status",
    [
        ({"speed": 10, "gear": "D", "brake": False, "error_code":0}, "OK"),
        ([{"speed": 10, "gear": "D", "brake": False, "error_code":0}], "INVALID"),
        ({"gear": "D", "brake": False, "error_code":0}, "INVALID"),
        ({"speed":10, "brake": False, "error_code":0}, "INVALID"),
        ({"speed":10, "gear": "D", "error_code":0}, "INVALID"),
        ({},"INVALID")
    ]
)
def test_state_utils_state_correct_output(state_dict,vehicle_status):
    assert parse_vehicle_state(state_dict) == vehicle_status

@pytest.mark.parametrize("state_dict, vehicle_status",
    [
        ({"speed": 10, "gear": "D", "brake": False, "error_code":0}, "OK"),
        ({"speed": 10.5, "gear": "D", "brake": False, "error_code":0}, "OK"),
        ({"speed": 0, "gear": "D", "brake": False}, "OK"),
        ({"speed": -1, "gear": "D", "brake": False, "error_code":0}, "INVALID"),
        ({"speed": "10", "gear": "D", "brake": False, "error_code":0}, "INVALID"),
    ]
)
def test_state_utils_speed_correct_output(state_dict,vehicle_status):
    assert parse_vehicle_state(state_dict) == vehicle_status
    
@pytest.mark.parametrize("state_dict, vehicle_status",
    [
        ({"speed": 0, "gear": "P", "brake": False, "error_code":0}, "OK"),
        ({"speed": 10, "gear": "N", "brake": False}, "OK"),
        ({"speed": 10, "gear": "D", "brake": False, "error_code":0}, "OK"),
        ({"speed": 10, "gear": "R", "brake": False, "error_code":0}, "OK"),
        ({"speed": 10, "gear": "r", "brake": False, "error_code":0}, "INVALID"),
        ({"speed": 10, "gear": "A", "brake": False, "error_code":0}, "INVALID"),
        ({"speed": 10, "gear": 2, "brake": False, "error_code":0}, "INVALID")
        
    ]
)
def test_state_utils_gear_correct_output(state_dict,vehicle_status):
    assert parse_vehicle_state(state_dict) == vehicle_status

@pytest.mark.parametrize("state_dict, vehicle_status",
    [
        ({"speed": 10, "gear": "D", "brake": False}, "OK"),
        ({"speed": 10, "gear": "D", "brake": True, "error_code":0}, "OK"),
        ({"speed": 10, "gear": "D", "brake": 1, "error_code":0}, "INVALID"),
        ({"speed": 10, "gear": "D", "brake": "False", "error_code":0}, "INVALID"),
        ({"speed": 10, "gear": "D", "brake": None, "error_code":0}, "INVALID")
    ]
)
def test_state_utils_brake_correct_output(state_dict,vehicle_status):
    assert parse_vehicle_state(state_dict) == vehicle_status

@pytest.mark.parametrize("state_dict, vehicle_status",
    [
        ({"speed": 10, "gear": "D", "brake": False, "error_code":0}, "OK"),
        ({"speed": 10, "gear": "D", "brake": False, "error_code":5}, "ERROR"),
        ({"speed": 10, "gear": "D", "brake": False, "error_code":-5}, "ERROR"),
        ({"speed": 10, "gear": "D", "brake": False, "error_code":"error"}, "INVALID"),
        ({"speed": 10, "gear": "D", "brake": False, "error_code":1}, "ERROR")
    ]
)
def test_state_utils_error_correct_output(state_dict,vehicle_status):
    assert parse_vehicle_state(state_dict) == vehicle_status

    