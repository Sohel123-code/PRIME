                            # instance methods

class laptop:
    stor='ssd'
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
    
    def get_info(self):
        print(f"The ram size {self.ram} with storage capacity {self.storage} of type {self.stor}")


l1=laptop(18,256)
l1.get_info()
# in instance metods we cn access the class atributes and instance attributes




