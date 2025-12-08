tup=(1,2,2,2,2,2,3,4,5,6,7)
sum=0
for val in tup:

    print(val)
    sum+=val

print(sum)


# methods of tuples
print(tup.index(3))

# count method is used to count all the occurances of the value in tupple
print(f"the occurances of 2 are {tup.count(2)}")


