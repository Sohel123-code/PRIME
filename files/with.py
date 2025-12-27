# when we open files they need to be closed so that data cant be loosed . so with the
# use of "with" when we open files they automatically get closed so that others cannot 
# manipulate the files 

with open("with.txt","r") as f:
    data =f.read()
    print(data)

    