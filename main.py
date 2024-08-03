from make_table import make_table
from calc_vdot import vdot
from training_paces import calc_paces
import pandas as pd

DISTANCE = 10000
UNITS = "m"
TIME = "39:00"


def main():
    # table = pd.DataFrame
    # table = make_table(20, 60, 0.1, "table.csv")
    table = pd.read_csv("table.csv")
    table = table.drop(table.columns[0], axis=1)
    # print(table.head())
    vd = vdot(DISTANCE, UNITS, TIME)
    equivalencies = table.loc[table["VDOT"]==vd]
    equivalencies = equivalencies.iloc[:, 2:]
    
    print("VDOT: {}".format(vd))
    
    print("Equivalent Performances")
    print(equivalencies.to_string(index=False))

    training_paces = calc_paces(vd)

if __name__ == "__main__":
    main()