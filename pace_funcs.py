def m_m(speed: float) -> str:
    """Converts meters per second to "MM:SS"
    Args:
        speed (float): m/s

    Returns:
        str: "HH:MM:
    """
    pace_list = list()
    conversion_factor = 60/1609.34
    mile_per_min = speed*conversion_factor
    min_per_mile = 1/mile_per_min

    minutes = int(min_per_mile//1)
    min_per_mile = min_per_mile%1
    seconds = int((min_per_mile*60))

    pace = f"{minutes:02}:{seconds:02}"

    return pace


def m_s(pace: str) -> float:
    """
    returns float of "MM:SS" converted to m/s, rounded to 2 decimal places
    pace: string in format "MM:SS"
    """
    meters = 1609.34
    seconds = 0
    time_list = pace.split(":")
    seconds += int(time_list[0])*60
    seconds += int(time_list[1])
    return round(meters/seconds,2)