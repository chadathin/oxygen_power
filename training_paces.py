import pandas as pd

def calc_paces(vdot: float) -> dict:
  # # VO2
  # numerator = -4.60 + 0.182258 * (m / t) + 0.000104 * (m / t)**2

  # # per cent
  # denominator = 0.8 + 0.1894393 * np.exp(-0.012778 * t) + 0.2989558 * np.exp(-0.1932605 * t)

  table = pd.read_csv("table.csv")
  print(table.head())
  
  fractions = {
    "easy": 0.66, # 59-74%
    "marathon": 0.80, # 75-84%
    "threshold": 0.86, # 83-88%
    "interval": 0.98 # 97-100%
  }

  paces = {
    "easy": 0,
    "marathon": 0,
    "threshold": 0,
    "interval": 0
  }

  for key in fractions:
    vdot_frac = round(vdot*fractions[key],1)
    lookup = table.loc[table["VDOT"] == vdot_frac, "1M"]
    print(lookup)
   # paces[key] = 
    
  print(paces)