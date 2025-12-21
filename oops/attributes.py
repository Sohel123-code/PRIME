#class atributes and instance atributes are there in python
class student :
    college="vignan"

    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa

stu1=student("sohel",9.8)


print(stu1.name)
print(stu1.cgpa)
# print(student.name) -----------> causes error

print(student.college)
print(stu1.college)

# hence object has more preference as both class and instance attributes can be called. but instance variables cant be
# called by class name