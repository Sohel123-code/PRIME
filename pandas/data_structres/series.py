import pandas as pd

# series are generally called as named 1-d arrays. they have labels to access the data

s=pd.Series([44,55,87,54])
print(s)
# index based accessing

print(s[0])

d=pd.Series([44,55,87,54],index=["sohel","raju","kumaar","teja"])
print(d)


# vectorized operations
s1=pd.Series([1,2,3,4,5])
s2=pd.Series([1,2,3,4,5])
print(s1+s2)

# we can change the elements but not the size of the array
s1[0]=100
print(s1)