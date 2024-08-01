from make_table import make_table
import pandas as pd

def main():
    table = pd.DataFrame
    table = make_table(30, 60, 0.1, "table.csv")
    print(table.head())

    

if __name__ == "__main__":
    main()