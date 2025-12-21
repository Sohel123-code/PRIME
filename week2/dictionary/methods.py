info={
    "NAME": "Mohamed khaja eshaq",
    "CGPA": 9.8,
    "BRANCH": "CSE",
    "SECTION": 4,
}
# we can get keys 

dict_keys=info.keys()
print(dict_keys)
 
 # we can get values
dict_values= info.values()
print(dict_values)

# coversion from dict_values to lists
dict_val=list(info.values())
print(dict_val)

# get items
info_item=list(info.items())

print(info_item)

# get keyword is used ,when supose if we use normal key directly and if key is not pesent then 
# it gives an error and remaining part of the  code never executes
# so to overcome this we have a built in method to get the  values by key


print(info.get("name"))
print(info.get("NAME"))


info.update({
    "city":"visakhapatnam"

})

print(info)
