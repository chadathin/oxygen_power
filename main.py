from make_table import make_table
from calc_vdot import vdot
from training_paces import calc_paces
from training_pace_percents import m_s, m_m, tp_percents
import pandas as pd

DISTANCE = 2
UNITS = "mi"
TIME = "15:22"


def main():
    # percents = tp_percents(35, 55)
    #
    # percents.to_csv("JD_percents.csv")
    # table = pd.DataFrame
    # table = make_table(20, 60, 0.1, "table.csv")
    table = pd.read_csv("table.csv")
    # table = table.drop(table.columns[0], axis=1)
    # print(table.head())

    vd = vdot(DISTANCE, UNITS, TIME)
    equivalencies = table.loc[table["VDOT"]==vd]
    equivalencies = equivalencies.iloc[:, 2:]
    
    print("VDOT: {}".format(vd))
    
    print("Equivalent Performances")
    print(equivalencies.to_string(index=False))

    training_paces = calc_paces(vd)

    for k,v in training_paces.items():
        print(f'{k}: {v[0]}-{v[1]}')

if __name__ == "__main__":
    main()