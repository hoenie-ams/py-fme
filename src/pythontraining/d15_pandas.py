"""
Demo of the pandas library
"""
import pandas as pd

df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])

df = pd.read_csv("https://raw.githubusercontent.com/pythonsherpa/data/master/sales.csv")
