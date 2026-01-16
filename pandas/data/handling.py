import pandas as pd

d=pd.read_csv("data.csv")

print(d,type(d))

e=pd.read_json("data1.json")
print(e,type(e))