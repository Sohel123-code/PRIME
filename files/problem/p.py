data = True
i=1
with open("p.txt","r") as f:
    while data:
        data=f.readline()

        if("python" in data):
            print(f"pyhon found at {i}")
        else:
            i=i+1

        



