# state_utils.py
def parse_vehicle_state(state):
    """
    Validates vehicle state dict. Returns:
    - "OK" if all fields valid and error_code==0/missing
    - "ERROR" if error_code is nonzero
    - "INVALID" for bad/missing data
    """
    allowed_gears = {"P", "N", "D", "R"}
    try:
        if not isinstance(state, dict):
            return "INVALID"
        if "speed" not in state or "gear" not in state or "brake" not in state:
            return "INVALID"
        speed = state["speed"]
        gear = state["gear"]
        brake = state["brake"]
        error_code = state.get("error_code", 0)
        if not isinstance(speed, (float, int)) or speed < 0:
            return "INVALID"
        if gear not in allowed_gears:
            return "INVALID"
        if not isinstance(brake, bool):
            return "INVALID"
        if not isinstance(error_code, int):
            return "INVALID"
        if error_code != 0:
            return "ERROR"
        return "OK"
    except Exception:
        return "INVALID"
