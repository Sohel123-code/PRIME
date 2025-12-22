f=open("sample.txt","a") # append mode
# it over writes the data 
f.write("this is the new data")

r =open("r.txt","x")  # x mode creates a new file
r.write("iam new data")

