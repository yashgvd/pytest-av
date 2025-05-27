from src.time_utils import is_monotonic
import pytest

@pytest.fixture(scope="module")
def sample_ts():
    return [1,2,3,4,5,6,7,8]

def test_is_monotonic_fixture(sample_ts):
    assert is_monotonic(sample_ts) == True
    
@pytest.mark.parametrize('timestamps, expected',[
    ([1,2,3],True),
    ([1.5,2,2.5],True),
    ([3,2,1],False),
    ([1.5,1.2,1.3],False),
    ([1e12,1e12+1,1e12+2],True),
    ]
)
def test_is_monotonic_correct_outputs(timestamps,expected):
    assert is_monotonic(timestamps) == expected
    


def test_is_monotonic_large_ts():
    assert is_monotonic([1e9,1e9+1,1e9+2]) == True
    
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
        
def test_is_monotonic_constant_value():
    assert is_monotonic([2,2,2,2]) == True


