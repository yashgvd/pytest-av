from checksum import is_valid_packet
import pytest

def test_packet_correct_checksum():
    packet = [1,2,3,6]
    assert is_valid_packet(packet) == True

def test_packet_incorrect_checksum():
    packet = [1,2,3,7]
    assert is_valid_packet(packet) == False

def test_packet_empty():
    packet = []    
    with pytest.raises(ValueError):
        is_valid_packet(packet)

def test_packet_non_integer():
    packet = [1,2,3,6.5]
    with pytest.raises(ValueError):
        is_valid_packet(packet)

def test_packet_non_list():
    packet = "not a list"
    with pytest.raises(ValueError):
        is_valid_packet(packet)
    with pytest.raises(ValueError):
        is_valid_packet(None)

def test_packet_value_out_of_range():
    packet = [1,2,3,300]
    with pytest.raises(ValueError):
        is_valid_packet(packet)
    with pytest.raises(ValueError):
        is_valid_packet([1, -5, 2, 3])

def test_packet_less_than_2_bytes():
    packet = [1]
    assert is_valid_packet(packet) == False
    
def test_packet_all_zero():
    packet = [0,0,0,0]
    assert is_valid_packet(packet) == True

def test_packet_all_max():
    # For [255, 255, 255], sum = 765, checksum = 765 % 256 = 253
    packet = [255, 255, 255, 253]
    assert is_valid_packet(packet) == True