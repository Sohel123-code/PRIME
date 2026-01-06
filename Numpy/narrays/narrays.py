import numpy as np

n=np.array([1,2,3,4,5])
print(n,type(n),n.dtype,n.shape)
n1=np.array([1,2,3,4,5,"prime"])
print(n,type(n1),n1.dtype,n1.shape)

# create arrays from scratch
a1=np.zeros((2,3),dtype="int64")
print(a1,a1.shape)

# prefill with ones
a2=np.ones((3,3),dtype="int64") 
print(a2,a2.shape)

# full function used to fill with particular value
a3=np.full((4,4),19)
print(a3,a3.shape)

# eye function used to create a square matrix
a4=np.eye(3)
print(a4)

# arrange function is similar to the range function in python
a5=np.arange(1,11)
print(a5,a5.shape)

a6=np.linspace(1,100,4)
print(a6,a6.shape)