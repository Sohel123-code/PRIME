class teacher:
    def __init__(self,salary):
        self.salary=salary

class student:
    def __init__(self,fees):
        self.fees=fees

class ta(teacher,student):
    def __init__(self,salary,fees,roll):
        super().__init__(salary)
        student.__init__(self,fees)
        self.roll=roll

t=ta(90000,4300,43)

print(t.salary,t.fees,t.roll)
