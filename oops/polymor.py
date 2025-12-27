# # polymorphism are of mianly 2 types :
# 1)function over-riding: when 2 classes are inherited their methods are redefined with the other paramters .

# function overvriding
class employee:
    def get_des(self):
        print(f"designation is employee")

class teacher(employee):
    def get_des(self):

        print(f"designation is teacher")


e=employee()
t=teacher()
e.get_des()
t.get_des()


# 2)duck typing  : here both clases which have the same method implementation are not inherited . they are implemented 
# individualy it is called as duck typing


class employee:
    def get_des(self):
        print(f"designation is employee")

class teacher():
    def get_des(self):

        print(f"designation is teacher")


e=employee()
t=teacher()
e.get_des()
t.get_des()


