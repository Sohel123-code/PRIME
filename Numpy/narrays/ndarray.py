import numpy as np
import time
size=10000000
li=list(range(size))
start=time.time()
sq=[x**2 for x in li]
end=time.time()
print(f"The time taken by list is {end - start}")

a=np.array(li)
st=time.time()
# vectorization
sq1=a**2
ed=time.time()
print(f"Time taken by nd array  is :{ed-st}")
if ed-st < end -start:
    print(f"Nd arrays are faster difference is {(end-start)-(ed-st)}")
else:
    print("python lists are faster")
