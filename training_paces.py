import pandas as pd
from pace_funcs import m_s, m_m

PER_CENT = 0.02

def calc_paces(vdot: float) -> dict:
  # # VO2
  # numerator = -4.60 + 0.182258 * (m / t) + 0.000104 * (m / t)**2

  # # per cent
  # denominator = 0.8 + 0.1894393 * np.exp(-0.012778 * t) + 0.2989558 * np.exp(-0.1932605 * t)

  table = pd.read_csv("table.csv")
  # print(table.head())

  # row = table.loc[table["VDOT"] == 30.2]
  # result = row["1M"]
  # print(result)
  
  fractions = {
    "easy": 0.66, # 59-74%
    "marathon": 0.79, # 75-84%
    "threshold": 0.85, # 83-88%
    "interval": 0.93 # 97-100%
  }

  # paces = {
  #   "easy": 0,
  #   "marathon": 0,
  #   "threshold": 0,
  #   "interval": 0
  # }

  paces = {
    "easy": list(),
    "marathon": list(),
    "threshold": list(),
    "interval": list()
  }

  for key in fractions:
    vdot_frac = round(vdot*fractions[key],1)
    row = table.loc[table["VDOT"] == vdot_frac]

    # get the training pace
    pace = row["1M"].values[0]

    # turn it to m/s
    speed = m_s(pace)

    hi = round(speed*(1+PER_CENT), 2)
    hi = m_m(hi)
    lo = round(speed*(1-PER_CENT), 2)
    lo = m_m(lo)

    paces[key].append(lo)
    paces[key].append(hi)

    # add % to m/s -> add to paces dict
    # subtract % to m/s -> add to paces dict


    # paces[key] = pace
  
  return paces
  # for key in paces:
  #   print("{}: {}".format(key,paces[key]))