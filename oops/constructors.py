# in_it method is a constructor in python
class student:
    subject="java"
    year="2nd"
    sec="d"
    def __init__(self,name,cgpa):
        # self paramter is used to store teh currrent instance 
        self.name=name
        self.cgpa=cgpa
        print(f"my name is {name} with CGPA {cgpa}")
        

stu1=student("rahul",7.8)
stu2=student("sohel",9.8)
stu3=student("khaja",10)

# if consrtructor has only 1 self parameter than it is called default constructor and more than 1 is called as 
# paramterized constructor

# in python one class can have only one constructor .
