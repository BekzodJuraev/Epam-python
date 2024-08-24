class Currency:


    pass





class Euro(Currency):

    def __init__(self,value):
        self.value=value

    @classmethod
    def course(cls,c):
        if c == Pound:
            return "100.0 GBP for 1 EUR"


class Dollar(Currency):

    def __init__(self,value):
        self.value=value

    @classmethod
    def course(cls, c):
        if c == Pound:
            return "100.0 GBP for 1 EUR"
class Pound(Currency):

    def __init__(self,value):
        self.value=value

    @classmethod
    def course(cls, c):
        if c == Pound:
            return "100.0 GBP for 1 EUR"

print(Euro.course(Pound))
