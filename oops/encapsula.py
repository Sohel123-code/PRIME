class bank:
    def __init__(self,name,add,balance):
        self.name=name  # public
        self._add=add # protected
        self.__balance=balance # private
# getters and setters are used to access the private memebers


    def get_bal(self):
        return self.__balance
    def set_bal(self,newbal):
        self.__balance=newbal


ac1=bank("sohel",100,9000)
ac2=bank("sonu",10,324242)
print(ac1.name,ac1._add,ac1.get_bal())
ac1.set_bal(10000)
print(ac1.get_bal())

# but we can access the private memberes in python easily
print(ac1.name,ac1._add,ac1._bank__balance)




