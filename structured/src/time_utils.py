# time_utils.py
def is_monotonic(timestamps):
    """
    Returns True if timestamps are monotonically increasing (each >= previous).
    Accepts a list of floats/ints (UNIX timestamps, ms, etc.).
    """
    if not isinstance(timestamps, list):
        raise ValueError("timestamps must be a list")
    if not timestamps:
        raise ValueError("timestamps cannot be empty")
    for t in timestamps:
        if not isinstance(t, (int, float)):
            raise ValueError("all timestamps must be int or float")
        if t <= 0:
            raise ValueError("timestamps should be greater than 0")
    if len(timestamps) == 1:
        return True  # trivially monotonic
    
    return all(curr >= prev for prev, curr in zip(timestamps, timestamps[1:]))
