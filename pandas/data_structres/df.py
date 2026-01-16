import pandas as pd
import numpy as np
# data frame can be created by dictionary of lists
info={
    "NAME":["Sohel","trilok","sai kiran"],
    "CGPA":[9.8,9.6,9.61]
}

df=pd.DataFrame(info)
print(df)

# data frame can be created by lists of lists
d=pd.DataFrame([["sohel",9.7],["trilok",9.66],["sai",9.68]  ],columns=["Name","SGPA"])

print(d)

# data frame creation using numpy arrays

e=np.array([["khaja",4,9.8],["Trilok",4,9.776],["Teja",4,9.66]])
t=pd.DataFrame(e,columns=["Name","Section","SGPA"])

print(t)
