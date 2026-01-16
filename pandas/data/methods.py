
import pandas as pd
import numpy as np
# these dataframe mathods are used to access the data esaily


d=pd.read_json("data1.json")


# head is used to return top 5 rows data
print(d.head())

# tail is used to return the bottom 5 rows data

print(d.tail())

#sample is used to return any random row values to get an idea

print(d.sample())


# info method is used to get information about the data

print(d.info())

#shape returns an tupple which conatains no of rows and columns  in the data frame

print(d.shape)

# describe method is used to make mathematicalo calculations on the maths data. it retruns the mean average etc


print(d.describe())

# columns is used to return values of the cloumns and nunique returns all the unique values of the rows

print(d.columns)
print(d.nunique())