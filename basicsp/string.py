word="python"
# string length
print(len(word))

#concatenate
word1="I love "

print(word1+word)

# char at index
print(word[2])


# slicing the string
print(word[1:4])

# if u want to go to end of the string then leave the column right side empty

# formatting in strings
a=5
b=10
sum=a+b
print("The sum is {}".format(sum))
print("THE SUM of {} and {} is {}".format(a,b,sum))

# index based formatting 

print("the sum of {1} and {0} is {2}".format(a,b,sum))
 
# value based formatting
print("there are {c} wonders in the world and {c} persons went to visit".format(c=7))

