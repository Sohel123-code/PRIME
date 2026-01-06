import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"The sum of the elements in columns are {np.sum(a,axis=0)}")
print(f"The sum of the elements in rows are {np.sum(a,axis=1)}")