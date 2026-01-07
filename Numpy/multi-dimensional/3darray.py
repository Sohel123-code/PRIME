import numpy as np

a=np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])
print(a,a.shape)

print(a[1,1,1])

print(a[:,1,:])

# 1st value in slicing is the  which 2d array we are going to choose and next value is row and
# next value is column value

# Broadcasting in NumPy is a feature that allows arrays of different shapes to be used together in arithmetic operations (like +, -, *, /) without explicitly copying data.

# 👉 NumPy automatically expands the smaller array so that both arrays have compatible shapes.

# In short

# Broadcasting = automatic shape adjustment of arrays for element-wise operations
