f = open("rp.txt","r+")

data=f.read()

f.write("this is the new data which had been added with the help of r plus mode")
print(data)