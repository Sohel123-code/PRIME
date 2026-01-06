import numpy as np
a=np.array([[1,2,3],[1,2,3],[1,2,3]])

print(a.shape,a.dtype,a.size,a.ndim)

# typr casting
int_a=a.astype(np.float64)
print(a)

# reshape is used to reshape the exisiting arrays
b=np.array([[1,2,3],[4,5,6]])
c=b.reshape(3,2)
print(c)

# flatten function is used to convert any 2-D array into 1-D array
d=b.flatten()
print(d)

# fancy indexing
f=np.array([1,2,3,4,5])
idx=[0,1,2]
print(f[idx])

# boolean indexing
print(f[f%2==0])


# slicing is also similar to lists
print(f[1:4])
print(f[1:])
# step
print(f[::2])
