"""
1) Create output dataframe with headings "easy, marathon, threshold, interval, rep"
    - rep = about 1-mile pace
2) Read in VDOT table
3) Loop through a list of vdots, by 0.1 increments
4) Feed times to `VDOT()` function
5) Feed VDOT() result to `training_paces()` function
    - This will return a `dict()` of the form:`"easy: [pace],
    "marathon": [pace]...` etc
6) Add each `dict` value to the output dataframe (as m/s)
7) Then, we want to divide each value in each row, by that row's `"threshold"` column, to find out each training pace's per cent of threshold value
    - This isn't a perfect replication of Daniels' training values, but it should be close enough
"""

from make_table import make_table
from calc_vdot import vdot
from training_paces import calc_paces
import pandas as pd

INTENSITIES = [
    "VDOT",
    "walking", 
    "easy", 
    "marathon", 
    "threshold", 
    "interval", 
    "reps"
    ]

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


def tp_percents(vd_start: int, vd_end: int) -> pd.DataFrame:
    # output = pd.DataFrame(columns=INTENSITIES)
    table = pd.read_csv("table.csv")
    vd_start = 39
    vd_end = 54
    walking = "18:00"
    
    results = list()
    for vd in range(vd_start*10, (vd_end+1)*10, 1):
        vdot_frac = vd/10

        # create list with vdo value as first entry
        paces = [vdot_frac]

        # append the walking speed (in m/s)
        paces.append(walking)

        # calculate easy, marathon, threshold and interval paces
        # using calc_paces() and append them to paces[]
        for item in list(calc_paces(vdot_frac).values()):
            paces.append(item)
        
        # Get an equivalent 1-mile pace from the VDOT table
        # append THAT to paces[]
        row = table.loc[table["VDOT"] == vdot_frac]
        col = row["1M"].values[0]
        paces.append(col)

        # Convert paces to m/s floats
        for i in range(1,len(paces)):
            paces[i] = m_s(paces[i])

        # Divide each by "threshold" column to find per cents
        thresh_loc = INTENSITIES.index("threshold")
        thresh = paces[thresh_loc]
        for i in range(1,len(paces)):
            paces[i] = round(paces[i]/thresh,2)
        results.append(paces)
    print(paces[0])
    
    # make a dataframe from the list of lists
    output = pd.DataFrame(data=results, columns=INTENSITIES)
    

    
    return output