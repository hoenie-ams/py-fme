"""
Demo of the pandas library
"""
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])
df = pd.read_csv("https://raw.githubusercontent.com/pythonsherpa/data/master/sales.csv")
var = 10
df["Profits"] = df["Sales"] - df["Costs"]
df.nlargest(10, columns=["Profits"]).plot(kind="bar", x="Country")
plt.show()

df.to_csv("sales.csv")
