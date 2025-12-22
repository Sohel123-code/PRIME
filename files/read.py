# file operation include reading and writing etc 
f=open("sample.txt","r")

data=f.read()

d=f.readline()
print(d)
print(data)

print(type(data))

f.close()

