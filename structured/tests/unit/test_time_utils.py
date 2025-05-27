from src.time_utils import is_monotonic
import pytest

def test_is_monotonic_correct_outputs():
    assert is_monotonic([1,2,3]) == True
    assert is_monotonic([3,2,1,2,3,4,5]) == False

def test_is_monotonic_not_list():
    with pytest.raises(ValueError):
        is_monotonic('time')

def test_is_monotonic_empty_list():
    with pytest.raises(ValueError):
        is_monotonic([])
        
def test_is_monotoic_single_element():
    assert is_monotonic([10.25]) == True

def test_is_monotonic_wrong_dtype_ts():
    with pytest.raises(ValueError):
        is_monotonic('abs')

def test_is_monotonic_negative_ts():
    with pytest.raises(ValueError):
        is_monotonic([-1,0,1,2,3])

