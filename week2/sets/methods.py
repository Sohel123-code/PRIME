# these are the methods in sets.

# add method we can add only 1 element
s={1,3,5,5,6,7,7,6,5}
s.add(9)
print(s)
# remove methods is to remove
s.remove(5)

print(s)

# pop function is used to remove any random value form the set
s.pop()
print(s)


# clear is used to clear all the elmenets of the set
s.clear()
print(s)



s1={1,2,4,5,6}
s2={6,9,5}

print(s1.union(s2))
print(s1.intersection(s2))
