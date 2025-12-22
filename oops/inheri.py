class employee:
    pas=1233
    def get_pass(self):
        return self.pas

    def change_pass(self,nes):
        self.pas=nes

class teacher(employee):
    def __init__(self,subject):
        self.subject=subject

class admin(employee):
    def __init__(self,role):
        self.role=role

t1=teacher("english")
t1.change_pass(4000)

a=admin("manager")
print(t1.subject,t1.get_pass())
print(a.role)