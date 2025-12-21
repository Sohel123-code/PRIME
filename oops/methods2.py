# class methods
class laptop:
    stor='ssd'
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
    @classmethod  # decorator
    def get_stor(cls):
        print(f"Storage type {cls.stor}")


l1=laptop(16,256)
laptop.get_stor()