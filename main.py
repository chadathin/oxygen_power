from make_table import make_table
from calc_vdot import vdot
import pandas as pd

def main():
    table = pd.DataFrame
    table = make_table(30, 60, 0.1, "table.csv")
    
    table = pd.read_csv("table.csv")
    print(table.head())

    vd = vdot(2, "mi", "12:00")
    
    print(vd)
    
    equivalencies = table["VDOT"] == vd
    print(table[equivalencies])
    

if __name__ == "__main__":
    main()