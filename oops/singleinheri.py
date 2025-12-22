
# single and multi level inheritance
class employee:
    start_time="9am"
    end_time="5pm"


class admin(employee):
    def __init__(self,role):
        self.role=role

class accountant(admin ):

    def __init__(self,role,salary):
        super().__init__(role)
        self.salary=salary

ac1=accountant("manager", 80000)
print(ac1.role,ac1.salary,ac1.start_time,ac1.end_time)