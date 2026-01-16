import pandas as pd

d=pd.read_csv("quality.csv")

print(d.head())
print(d.describe())

print(d[["state","location"]])



