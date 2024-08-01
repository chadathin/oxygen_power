from make_table import make_table
from calc_vdot import vdot
from training_paces import calc_paces
import pandas as pd

def main():
    # table = pd.DataFrame
    # table = make_table(30, 60, 0.1, "table.csv")
    
    table = pd.read_csv("table.csv")
    # print(table.head())

    vd = vdot(5000, "m", "24:00")
    
    print(vd)
    
    equivalencies = table["VDOT"] == vd
    # print(table[equivalencies])

    training_paces = calc_paces(vd)
    

if __name__ == "__main__":
    main()