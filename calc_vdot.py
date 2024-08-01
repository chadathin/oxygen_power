import numpy as np
MILES_TO_METERS = 1609.34

COMMON_DISTANCES = {
    3.1: 5000,
    6.2: 10000,
    13.1: 21097.5,
    26.2: 42195
}

def vdot(dist: float, units: str, time: str) -> float:
    minutes = 0
    has_hours = False
    # print(list(COMMON_DISTANCES.keys()))
    # Check for common distances in imperial units
    if units == "mi" and dist in list(COMMON_DISTANCES.keys()):
        dist = COMMON_DISTANCES[dist]
    
    # convert distance to meters
    elif units == "km":
        dist *= 1000
    elif units == "mi":
        dist *= MILES_TO_METERS
        
    # convert "HH:MM:SS" to minutes
    time_list = time.split(":")
    if len(time_list) == 3:
        has_hours = True
    if has_hours:
        minutes += int(time_list[0])*60
        minutes += int(time_list[1])
        minutes += round(int(time_list[2])/60,2)
    else:
        minutes += int(time_list[0])
        minutes += round(int(time_list[1])/60,2)
    
    numerator = -4.60 + 0.182258 * (dist / minutes) + 0.000104 * (dist / minutes)**2
    denominator = 0.8 + 0.1894393 * np.exp(-0.012778 * minutes) + 0.2989558 * np.exp(-0.1932605 * minutes)
    
    return round(numerator/denominator,1)
    
    return vdot