import numpy as np
import sys
# size comparison of lists and nd arrays

size=10000000
li=list(range(size))
print(f"The size is {sys.getsizeof(li)*len(li)} Bytes")
s=sys.getsizeof(li)*len(li)


a=np.array(li)
print(f"The size of ndarray is {sys.getsizeof(a)*len(a)} Bytes")
s1=sys.getsizeof(a)*len(a)
if s1<s:
    print("nd arrays takes less space")
else:
    print("lists take more space")
