# packet_utils.py
def is_valid_packet(packet):
    """
    Returns True if packet checksum matches.
    The checksum is the sum of all bytes except the last, modulo 256.
    The last byte is the provided checksum.
    """
    if not isinstance(packet, list):
        raise ValueError("packet must be a list")
    if not packet:
        raise ValueError("packet cannot be empty")
    if any(not isinstance(b, int) or b < 0 or b > 255 for b in packet):
        raise ValueError("all packet elements must be bytes (0-255)")
    if len(packet) < 2:
        return False  # Too short to have data+checksum
    # checksum = sum(packet[:-1]) % 256
    
    data_sum = sum(packet[:-1])
    checksum = data_sum % 256
    
    return checksum == packet[-1]
