import numpy as np
ar_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ar_2d,ar_2d.shape)

ar_2d1=np.array([[1,2,3],[3,4,3],[3,43,2],[1,3,2]])
print(ar_2d1,ar_2d1.shape)


# functions used to create nd arrays from scratch
a1=np.zeros((2,3),dtype="int64")
print(a1)
a2=np.ones((3,3), dtype="int64") # normalyy it creates into float
print(a2)
a3=np.full((3,3),100) # used to create a matrix with given pass value
print(a3)
a4=np.eye(3) # used to create a identity matrix
print(a4)
a5=np.arange(0,10) # like range funtion
print(a5)
a6=np.linspace(1,100,4)
# used to create a evenly spaced array from given starting integer to last integer
print(a6)