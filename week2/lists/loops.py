num=[23,26,87,97,43,32]
for i in num:
    print(i)

# Linear search
x=43
idx=0
for val in num:
    if(x==val):
        print(f"value found at index :{idx}")
        break
    idx+=1
    

       