import numpy as np
import pandas as pd


def open_file(file):
    df = pd.read_csv(file, sep="\t", names=["Time", "Angle"])
    return df
