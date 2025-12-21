
class store:
    tcount=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        store.tcount += 1
    
    def get_info(self):
        print(f"the price of the {self.name} is {self.price}")

    @classmethod
    def count(cls):
        print(f"Total no of products are {cls.tcount}")


    


c1=store("phone",46000)
c2=store("laptop",780000)
c3=store("TV",7800232)
c1.get_info()
c2.get_info()
c3.get_info()
store.count()




