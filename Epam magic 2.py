class Bird:
    def __init__(self,name):
        self.name=name

    def fly(self):
        pass

    def walk(self):
        return f"{self.name} bird can walk"

class FlyingBird(Bird):
    def __init__(self,name,ration="grains"):
        self.name=name
        self.ration=ration

    def eat(self):
        return f"It eats mostly {self.ration}"


    def __str__(self):
        return f"{self.name} bird can walk and fly"

class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration="grains"):
        self.name = name
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def fly(self):
       return f"AttributeError: '{self.name}' object has no attribute 'fly'"


class SuperBird(FlyingBird):
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration


b=Bird("Any")
print(b.walk())

c=FlyingBird("Canary")
print(c)
print(c.fly())


p = NonFlyingBird("Penguin", "fish")
print(p.swim())
print(p.fly())
print(p.eat())

s=SuperBird("Gull")
print(s)
print(s.eat())
