class student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def give_cgpa(self):
        # self is used to push the required object at a time
        print(f"my cgpa is {self.cgpa}")

stu1=student("sohel",9.8)
stu2=student("trilok",9.61)
stu3=student("sai",9.63)

stu1.give_cgpa()
stu2.give_cgpa()
stu3.give_cgpa()






