# x mode in files is used to create a new file and write the data in the new file
# the main difference between x mode and w mode is . when file already exists in the file manager 
# then x throws an error that file exists already , but in write mode it truncates the whole data.

f= open("xmode.txt","x")

f.write("hi this is the data which is added with the help of the xd mode")