import numpy as np
import pandas as pd
import os

# Define the function f(t)
def f(t, m, R):
    try:
        
        # VO2
        numerator = -4.60 + 0.182258 * (m / t) + 0.000104 * (m / t)**2
        
        # per cent
        denominator = 0.8 + 0.1894393 * np.exp(-0.012778 * t) + 0.2989558 * np.exp(-0.1932605 * t)
        return (numerator / denominator) - R
    except OverflowError:
        return np.inf

# Define the derivative f'(t)
def f_prime(t, m):
    try:
        numerator = -4.60 + 0.182258 * (m / t) + 0.000104 * (m / t)**2
        denominator = 0.8 + 0.1894393 * np.exp(-0.012778 * t) + 0.2989558 * np.exp(-0.1932605 * t)

        d_numerator_dt = -0.182258 * (m / t**2) - 0.000208 * (m**2 / t**3)
        d_denominator_dt = 0.1894393 * 0.012778 * np.exp(-0.012778 * t) + 0.2989558 * 0.1932605 * np.exp(-0.1932605 * t)

        return (d_numerator_dt * denominator - numerator * d_denominator_dt) / (denominator ** 2)
    except OverflowError:
        return np.inf

# Newton-Raphson method
def newton_raphson(m, R, initial_guess=3.0, tolerance=1e-8, max_iterations=1000):
    t = initial_guess
    for _ in range(max_iterations):
        f_t = f(t, m, R)
        f_prime_t = f_prime(t, m)

        if f_prime_t == np.inf:
            raise ValueError("Overflow encountered in computation. No solution found.")
        if f_prime_t == 0:
            raise ValueError("Derivative is zero. No solution found.")

        t_next = t - f_t / f_prime_t

        if abs(t_next - t) < tolerance:
            return round(t_next,2)

        t = t_next

        # Ensure t stays within a reasonable range to avoid overflow
        if t < 1e-6:
            t = 1e-6
        elif t > 1e6:
            t = 1e6

    raise ValueError("Maximum iterations exceeded. No solution found.")

def format_minutes(time: float)-> str:
    if time >= 60:
        hours = int(time//60)
        minutes = int(time-(hours*60))
        seconds = int((time%1)*60)
        return "{:d}:{:02d}:{:02d}".format(hours,minutes,seconds)
    else:
        minutes = int(time)
        seconds = int((time%1) * 60)
        return "{:02d}:{:02d}".format(minutes,seconds)

def make_table(start: int, end: int, step: float, f_name: str) -> pd.DataFrame:
    """
    start:
    end:
    step:
    float:
    """

    DISTANCES = {
        "1K": 1000,
        "1M": 1609.34,
        "3K": 3000,
        "5K": 5000,
        "8K": 8000,
        "10K": 10000,
        "10M": 16093.4,
        "Half": 21097.5,
        "Full": 42195
    }

    cols = ["VDOT"]
    for key in list(DISTANCES.keys()):
        cols.append(key)

    start_int = int(start*10)
    end_int = int(end*10)
    step_int = int(step*10)
    
    table = dict()
    table["VDOT"] = list()

    # Populate table["VDOT"] with all the values we'll be tabluating
    for i in range(start_int, end_int+1, step_int):
        table["VDOT"].append(i/10)

    # Populate table with the values of f(v) for each v
    
    for key in list(DISTANCES.keys()):
        table[key] = list()
        for v in table["VDOT"]:
            root = round(newton_raphson(DISTANCES[key], v),2)
            time = format_minutes(root)
            table[key].append(time)
                        
    
    table = pd.DataFrame(table, columns=cols)
    table.to_csv("./"+f_name)
    return None
    
    # if os.path.isfile("./"+f_name):
    #     print("Error: File already exists")
    #     return -1
    # else:
    #     table.to_csv("./"+f_name)
    #     print("File created successfully")
    #     return 0