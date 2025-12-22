from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class lion(animal):
    def make_sound(self):
        print("roar")


class cow(animal):
    def make_sound(self):
        print("moo")

l=lion()
c=cow()
l.make_sound()
c.make_sound()