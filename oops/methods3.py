#static methods

class laptop:
    stor='ssd'
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
    
    def get_info(self):
        print(f"The ram size {self.ram} with storage capacity {self.storage} of type {self.stor}")
    
    @staticmethod
    def cal_price(price,discount):
        fp=price-(discount*price/100)
        print(fp)


l1=laptop(18,256)

# static methods cant use both class and instance parameters.

l1.cal_price(40000,10)