# vehicle_utils.py
def compute_speed(ticks: int, interval_sec: float, wheel_circumference_m: float) -> float:
    """
    Calculate speed in m/s given number of encoder ticks, time interval in seconds,
    and wheel circumference.
    """
    if not isinstance(ticks, int):
        raise ValueError("ticks must be an integer")
    if interval_sec <= 0:
        raise ValueError("interval_sec must be positive")
    if wheel_circumference_m <= 0:
        raise ValueError("wheel_circumference_m must be positive")
    
    rotations = ticks / 1024   # Assume 1024 ticks per wheel revolution
    distance = rotations * wheel_circumference_m
    return distance / interval_sec
