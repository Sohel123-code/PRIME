import numpy as np
a=np.array([1,2,3,4,5])

# mathematical functions

print(np.sum(a))
print(np.prod(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.var(a))
print(np.std(a))
# returns index of min and max
print(np.argmin(a))
print(np.argmax(a))

# powers
print(np.sqrt(a))
print(np.square(a))
print(np.pow(a,3))

# log

print(np.log(a))
print(np.log10(a))# base 10
print(np.exp(a))

# round
print(np.round(3.14))
print(np.ceil(3.14))
print(np.floor(3.14))
print(np.abs(-3.14))

# unique and sort
print(np.unique(a))